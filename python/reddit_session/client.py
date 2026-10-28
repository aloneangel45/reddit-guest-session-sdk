import requests
from typing import Dict, Any

class RedditSessionClient:
    """Enterprise client for Reddit Guest Session & OAuth Bearer extraction."""
    
    def __init__(self, rapidapi_key: str, host: str = "reddit-data-harvester-guest-session-api.p.rapidapi.com"):
        self.rapidapi_key = rapidapi_key
        self.host = host
        self.base_url = f"https://{host}/api/v1/reddit"

    def get_guest_session(self) -> Dict[str, Any]:
        """Acquire anonymous Reddit OAuth 2.0 bearer token and session cookies."""
        headers = {
            "x-rapidapi-host": self.host,
            "x-rapidapi-key": self.rapidapi_key,
            "Content-Type": "application/json"
        }
        response = requests.post(f"{self.base_url}/guest-session", headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
