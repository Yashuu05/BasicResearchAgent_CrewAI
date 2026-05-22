from dotenv import load_dotenv
import os, sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from src.crewai_project.logger import logging

API = load_dotenv("TAVILY_API_KEY")
if API is not None:
    print("API key loaded successfully")
    logging.info("Tavily API Key successfully found.")
else:
    print("API key not found. Check .env file")
    logging.error("No API key Found for Tavily")