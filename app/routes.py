from flask import Blueprint, jsonify
from app.config import Config
from app.services.pokeapi import PokeAPIClient
from app.services.processor import PokemonProcessor
from app.services.repository import PokemonRepository

bp = Blueprint("pokemon", __name__)

client = PokeAPIClient(Config.POKEAPI_BASE_URL)


@bp.route("/scout", methods=["POST"])
def scout_pokemon():
    """
    Fetch, process, and store Pokémon data.
    Uses the default Pokémon list from config.
    """
    results = []

    for name in Config.DEFAULT_POKEMON:
        raw_data = client.get_pokemon(name)
        sanitized = PokemonProcessor.sanitize(raw_data)

        existing = PokemonRepository.get_by_pokemon_id(
            sanitized["pokemon_id"]
        )

        if existing:
            results.append(
                {"name": name, "status": "already_exists"}
            )
            continue

        PokemonRepository.create(sanitized)
        results.append(
            {"name": name, "status": "created"}
        )

    return jsonify(results), 201


@bp.route("/pokemon", methods=["GET"])
def list_pokemon():
    """
    List all stored Pokémon.
    """
    pokemon = PokemonRepository.get_all()

    return jsonify([
        {
            "pokemon_id": p.pokemon_id,
            "name": p.name,
            "types": p.types,
            "stats": p.stats,
            "abilities": p.abilities,
            "height": p.height,
            "weight": p.weight,
        }
        for p in pokemon
    ])
