import json
import re
from typing import Any, Callable, Dict, List, Optional

from openai import OpenAI

# Load metadata from JSON file
def load_metadata(filepath: str) -> Dict[str, Any]:
    """
    Load metadata from a given JSON file path.

    Args:
        filepath (str): The path to the JSON file containing metadata.

    Returns:
        Dict[str, Any]: A dictionary representation of the metadata from the JSON file.
    """
    with open(filepath, "r") as f:
        metadata = json.load(f)
    return metadata


class ChatBot:
    """
    A simple chatbot that interacts with a conversation history using a specified protocol.
    """

    def __init__(self, protocol: str, api_key: str):
        """
        Initialize the ChatBot with a specified protocol and API key.

        Args:
            protocol (str): The initial instructions or rules for the chatbot.
            api_key (str): The API key for accessing OpenAI services.
        """
        self.client = OpenAI(
            api_key=api_key
        )  # Initialize the OpenAI client with the given API key
        self.protocol = protocol  # Store the protocol for this chatbot instance
        self.history = [{"role": "system", "content": self.protocol}]
        # Initialize conversation history with protocol as the starting message

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the chatbot based on the user's input.

        Args:
            prompt (str): The user's message to which the chatbot should respond.

        Returns:
            str: The chatbot's generated response.
        """
        # Add user's message to the conversation history
        self.history.append({"role": "user", "content": prompt})

        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=self.history,  # Request a completion from the AI model
        )

        response = completion.choices[0].message.content  # Extract the response content
        self.history.append({"role": "assistant", "content": response})
        # Append the chatbot's response to the conversation history

        return response  # Return the generated response

    def get_history(self) -> List[Dict[str, str]]:
        """
        Retrieve the conversation history.

        Returns:
            List[Dict[str, str]]: A list of messages in the conversation history.
        """
        return self.history  # Return the complete conversation history


def match_trigger_words(user_message: str, trigger_words: List[str]) -> bool:
    """
    Check if all words in each trigger phrase are present in the user's message.

    Args:
        user_message (str): The message input by the user.
        trigger_words (List[str]): A list of phrases to be matched against the user's message.

    Returns:
        bool: True if all words in at least one trigger phrase are found in the user's message.
    """
    # Clean the user message by removing punctuation and converting to lowercase
    cleaned_message = re.sub(r"[^\w\s]", "", user_message.lower())
    message_words = cleaned_message.split()  # Split message into individual words

    for trigger in trigger_words:
        cleaned_trigger = re.sub(r"[^\w\s]", "", trigger.lower())
        trigger_words_list = cleaned_trigger.split()  # Split trigger phrase into words

        # Check if all words in the trigger phrase are present in the user message
        if all(word in message_words for word in trigger_words_list):
            print(f"Match found for trigger: '{trigger}'")
            return True

    # print("No match found.")
    return False


def intent_processor(
    event_stream: List[Dict[str, Any]], metadata: Dict[str, Any], bot: ChatBot
) -> None:
    """
    Process the event stream to detect any user intents by matching trigger words from
    metadata. If an intent is detected, append an API call to the event stream; otherwise,
    use the chatbot to generate a response.

    Args:
        event_stream (List[Dict[str, Any]]): A list of events representing the conversation history.
        metadata (Dict[str, Any]): Metadata containing API information and trigger words for intents.
        bot (ChatBot): An instance of a chatbot to generate responses when no intent is detected.

    Returns:
        None: The function modifies the event_stream in place.
    """
    # Find the latest user message from the event stream
    last_event = next(
        (
            event
            for event in reversed(event_stream)
            if event.get("event") == "user_message"
        ),
        None,
    )

    if not last_event:
        print("👀 No user message found in event stream.")
        return

    user_message = last_event.get("content", "")

    # Iterate through all functions in metadata and check if trigger words are present
    for api_name, api_metadata in metadata.items():
        trigger_words = api_metadata.get("trigger_word", [])

        # Check if any trigger word matches the user message
        if match_trigger_words(user_message, trigger_words):
            print(f"👀 Intent detected for API call: {api_name}")

            # Append the API call to the event stream
            event_stream.append(
                {
                    "intent_processor": "api_call",
                    "api_name": api_name,
                    "response": {"status": "none"},
                }
            )
            break
    else:
        # No intent detected, use the bot for a general conversation
        bot_response = bot.generate_response(user_message)
        print(f"🤖 Bot Response: {bot_response}")
        event_stream.append({"event": "assistant_message", "content": bot_response})


# Function registry to map API names to actual function calls
function_registry: Dict[str, Callable[..., Dict[str, Any]]] = {}


def register_function(api_name: str):
    """
    Decorator to register API functions dynamically into the function registry.

    Args:
        api_name (str): The name of the API function to be registered in the function_registry.

    Returns:
        Callable: A decorator that registers the provided function under the given api_name.
    """

    def decorator(func: Callable[..., Dict[str, Any]]):
        """
        Registers the given function into the function_registry with the specified api_name.

        Args:
            func (Callable[..., Dict[str, Any]]): The function to be registered.

        Returns:
            Callable: The original function passed to the decorator.
        """
        function_registry[api_name] = func
        return func

    return decorator


def find_in_event_stream(
    key: str, event_stream: List[Dict[str, Any]], current_api_name: str
) -> Optional[str]:
    """
    Helper function to find a piece of information in the event stream.
    Searches in reverse order for the most recent occurrence of a matching key.
    Stops when any 'success' status is encountered, meaning that information is already used.

    Args:
        key (str): The key to search for.
        event_stream (List[Dict[str, Any]]): The event stream containing user and API call events.
        current_api_name (str): The name of the current API call to handle context-specific data.

    Returns:
        Optional[str]: The content of the user message matching the key, or None if not found.
    """
    for event in reversed(event_stream):
        # Stop the search if an API call with a 'success' status is found for any API
        if event.get("event") == "api_call" and "success" in event.get(
            "response", {}
        ).get("status", ""):
            break

        # Continue searching user messages
        if (
            event.get("event") == "user_message"
            and key.lower() in event.get("content", "").lower()
        ):
            return event.get("content")

    return None


def resolve_and_execute(
    event_stream: List[Dict[str, Any]],
    metadata: Dict[str, Any],
    secrets: Dict[str, str],
) -> Optional[Dict[str, Any]]:
    """
    Resolve dependencies and execute the specified API call dynamically.
    Only runs if the last event in the event_stream has 'intent_processor': 'api_call'.

    Args:
        event_stream (List[Dict[str, Any]]): A list containing event data such as user messages or API calls.
        metadata (Dict[str, Any]): Metadata with definitions for the APIs that can be called, including payload structures.
        secrets (Dict[str, str]): A dictionary of secrets or credentials required for executing API calls.

    Returns:
        Optional[Dict[str, Any]]: The result of the executed API function, or None if an error occurs.
    """
    api_event = next(
        (
            event
            for event in reversed(event_stream)
            if event.get("intent_processor") == "api_call"
        ),
        None,
    )

    if not api_event:
        print("👀 No API call found in the event stream. Exiting.")
        return None

    api_name = api_event.get("api_name")
    if not api_name or api_name not in metadata:
        print(f"👀 Error: API '{api_name}' is not defined in the metadata.")
        return None

    payload = {}
    for key in metadata[api_name]["sample_payload"]:
        # Pass the current API name to maintain context
        value = find_in_event_stream(key, event_stream, current_api_name=api_name)
        if not value:
            value = input(f"Please provide {key}: ")
            event_stream.append(
                {"event": "user_message", "content": f"My {key} is {value}."}
            )
        payload[key] = value.split(" is ")[-1]

    api_function = function_registry.get(api_name)
    if api_function:
        return api_function(
            payload, secrets, event_stream
        )  # Pass event_stream as argument
    else:
        print(f"👀 Error: No function found for API call '{api_name}'.")
        return None
