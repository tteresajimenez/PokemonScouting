from app.config import Config
from app.services.pokeapi import PokeAPIClient

client = PokeAPIClient(Config.POKEAPI_BASE_URL)
