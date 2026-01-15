import os


class Config:
    """Base application configuration"""

    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///pokemon.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # External APIs
    POKEAPI_BASE_URL = os.getenv(
        "POKEAPI_BASE_URL",
        "https://pokeapi.co/api/v2"
    )

    # Default scouting targets (can be overridden)
    DEFAULT_POKEMON = [
        "pikachu",
        "dhelmise",
        "charizard",
        "parasect",
        "aerodactyl",
        "kingler",
    ]
