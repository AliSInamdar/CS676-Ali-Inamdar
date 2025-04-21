import secrets
from typing import Any, Dict, List
import io
import contextlib
import openai
import pandas as pd
import os
import re
from mistralai.client import MistralClient
from dotenv import load_dotenv

load_dotenv()


from serpapi import GoogleSearch

from project3.helper import register_function

@register_function("google_search")
def google_search(
    payload: Dict[str, str], secrets: Dict[str, str], event_stream: list
) -> Dict[str, Any]:
    """
    Simulate a Google search using the SerpAPI and return the results formatted as a Markdown table.

    Args:
        payload (Dict[str, str]): A dictionary containing the search parameters:
                                  - query: The search query string.
                                  - location: The location for the search.
        secrets (Dict[str, str]): Contains the SerpAPI key for API authentication.
        event_stream (list): A list used to log events and responses.

    Returns:
        Dict[str, Any]: A dictionary with the status of the API call and a Markdown table of search results.
    """

    # Extract Secrets
    serpapi_key = secrets["serpapi_key"]

    # Extract search parameters from the payload
    engine = payload.get("engine", "google")
    query = payload.get("query", "")
    location = payload.get("location", "")
    num = payload.get("num", "50")
    num = int(num)
    num = num if type(num) == int else 50

    # Checkpoint
    print(f"Run google search API using: \nquery={query}, \nlocation={location}")

    try:
        # Perform the Google Search using SerpAPI
        search = GoogleSearch(
            {
                "engine": engine,
                "q": query,
                "location": location,
                "api_key": serpapi_key,
                "num": num,
            }
        )
        results = search.get_dict()

        # Extract relevant results
        organic_results = results.get("organic_results", [])

        # Convert search results to a Markdown table
        md_table = "| Title | Link | Snippet |\n| :--- | :--- | :--- |\n"
        for item in organic_results:
            title = item.get("title", "N/A")
            link = item.get("link", "#")
            snippet = item.get("snippet", "N/A")
            md_table += f"| {title} | [Link]({link}) | {snippet} |\n"
        print(f"👀 Results: \n{md_table}")

        # Prepare the response
        response = {"status": "success", "model_name": "None", "results": md_table}

        # Append the result to the event stream
        event_stream.append(
            {
                "event": "api_call",
                "api_name": "google_search",
                "response": {"text": response, "status": "200 success"},
            }
        )

    except Exception as e:
        # Handle any exceptions that occur during the API call
        response = {"status": f"error: {str(e)}", "model_name": "None"}
        event_stream.append(
            {"event": "api_call", "api_name": "google_search", "response": response}
        )

    return response


@register_function("python_code")
def python_code(
    payload: Dict[str, str], secrets: Dict[str, str], event_stream: list
) -> Dict[str, Any]:
    """
    Generate Python code using OpenAI API based on a prompt.
    """
    openai_api_key = secrets.get("openai_api_key")
    openai.api_key = openai_api_key

    prompt = payload.get("prompt", "")
    model = payload.get("model", "gpt-4")

    print(f"🚀 Prompt received: {prompt}")

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a Python code generator.you need system prompt to consume the event stream which is in the payload (this is in the input arg of this func), you need a prompt engineer here to isntruct LLM to give you py code in one blob "}, # you need system prompt to consume the event stream which is in the payload (this is in the input arg of this func), you need a prompt engineer here to isntruct LLM to give you py code in one blob
                {"role": "user", "content": f"Generate Python code for:\n{prompt}"}
            ],
            temperature=0.9,
            max_tokens=500,
        )

        code = response['choices'][0]['message']['content'].strip()
        #if code exists execute 
        exec_output = None
        if code:
            try:
                # Strip markdown formatting if needed
                if code.startswith("```python"):
                    code = code.strip("```python").strip("```").strip()
                
                # Capture printed output from code
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    exec(code, {})  # run in an isolated global namespace
                exec_output = buffer.getvalue()

            except Exception as exec_err:
                exec_output = f"Execution error: {str(exec_err)}"
        result = {
            "status": "success",
            "model_name": model,
            "generated_code": f"```python\n{code}\n```"
        }

        event_stream.append({
            "event": "api_call",
            "api_name": "python_code",
            "response": {"text": result, "status": "200 success"},
        })

    except Exception as e:
        result = {"status": f"error: {str(e)}", "model_name": model}
        event_stream.append({
            "event": "api_call",
            "api_name": "python_code",
            "response": result,
        })

    return result
