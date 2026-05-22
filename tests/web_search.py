from dotenv import load_dotenv
import os, sys
from tavily import TavilyClient
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from src.crewai_project.logger import logging as log

log.info("Initialized web search test")

# Load variables from .env
load_dotenv()
# Access the API key
api_key = os.getenv("TAVILY_API_KEY")

if api_key is not None:

    tavily_client = TavilyClient(api_key=api_key)
    print("API key loaded successfully")
    log.info("API key found.")
    response = tavily_client.search("Who is Leo Messi?")
    print(response)
    print("\ntype :", type(response))
    log.info("Web search successful")

else:
    log.error("Tavily API failed to load")
    print("Error! API key not found.")