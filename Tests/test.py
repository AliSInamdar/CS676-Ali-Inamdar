import os
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
MISTRAL_API_KEY= os.getenv("MISTRAL_API_KEY")

# Import the agent
from project3.main import AgentX

# Initialize and start the chat!
agent = AgentX(
    openai_api_key=OPENAI_API_KEY,
    serpapi_key=SERPAPI_API_KEY,
    protocol="You are a helpful assistant.",
)

# Run the chat
agent.start_chat()
