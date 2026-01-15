import requests
from typing import Dict


class PokeAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get_pokemon(self, name: str) -> Dict:
        """
        Fetch raw Pokémon data from PokeAPI.
        Raises HTTPError on non-200 responses.
        """
        url = f"{self.base_url}/pokemon/{name.lower()}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
