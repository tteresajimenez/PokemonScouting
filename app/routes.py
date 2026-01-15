from flask import Blueprint, jsonify, request, current_app
from app.config import Config
from app.services.pokeapi import PokeAPIClient
from app.services.processor import PokemonProcessor
from app.services.repository import PokemonRepository

bp = Blueprint("pokemon", __name__)

client = PokeAPIClient(Config.POKEAPI_BASE_URL)


@bp.route("/scout", methods=["POST"])
def scout_pokemon():
    results = []

    pokemon_list = current_app.config["DEFAULT_POKEMON"]

    for name in pokemon_list:
        raw_data = client.get_pokemon(name)
        sanitized = PokemonProcessor.sanitize(raw_data)

        existing = PokemonRepository.get_by_pokemon_id(
            sanitized["pokemon_id"]
        )

        if existing:
            results.append({"name": name, "status": "already_exists"})
            continue

        PokemonRepository.create(sanitized)
        results.append({"name": name, "status": "created"})

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

@bp.route("/pokemon", methods=["POST"])
def add_pokemon():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "Pokemon name is required"}), 400

    raw = client.get_pokemon(name)
    sanitized = PokemonProcessor.sanitize(raw)

    existing = PokemonRepository.get_by_pokemon_id(
        sanitized["pokemon_id"]
    )
    if existing:
        return jsonify({"status": "already_exists"}), 200

    PokemonRepository.create(sanitized)
    return jsonify({"status": "created", "name": name}), 201

@bp.route("/pokemon/<name>", methods=["DELETE"])
def delete_pokemon(name):
    deleted = PokemonRepository.delete_by_name(name)
    if not deleted:
        return {"error": "Not found"}, 404
    return "", 204