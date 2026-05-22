from dotenv import load_dotenv
from tavily import TavilyClient

API = load_dotenv("TAVILY_API_KEY")
if API is not None:
    print("API key loaded successfully")
else:
    print("API key not found. Check .env file")