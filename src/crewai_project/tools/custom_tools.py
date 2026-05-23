from crewai.tools import BaseTool
from tavily import TavilyClient
import os

class TavilySearchTool(BaseTool):
    name: str = "Tavily Web Search"
    description: str = "Search the web for information using the Tavily API. Useful for finding up-to-date information."

    def _run(self, query: str) -> str:
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            return "Error: TAVILY_API_KEY environment variable not set."
        
        try:
            client = TavilyClient(api_key=api_key)
            # You can customize the response format. We use search by default.
            response = client.search(query=query)
            
            # Format the output so the agent can easily read it
            results = response.get("results", [])
            formatted_results = ""
            for res in results:
                formatted_results += f"Title: {res.get('title', 'No Title')}\n"
                formatted_results += f"URL: {res.get('url', 'No URL')}\n"
                formatted_results += f"Content: {res.get('content', 'No Content')}\n\n"
                
            return formatted_results if formatted_results else "No results found."
        except Exception as e:
            return f"Error during search: {str(e)}"
