from typing import Dict


class PokemonProcessor:
    @staticmethod
    def sanitize(raw_data: Dict) -> Dict:
        """
        Transform raw PokeAPI data into a sanitized format
        suitable for persistence and scouting analysis.
        """

        return {
            "pokemon_id": raw_data["id"],
            "name": raw_data["name"],

            "types": [
                t["type"]["name"]
                for t in raw_data.get("types", [])
            ],

            "abilities": [
                a["ability"]["name"]
                for a in raw_data.get("abilities", [])
            ],

            "stats": {
                stat["stat"]["name"]: stat["base_stat"]
                for stat in raw_data.get("stats", [])
            },

            "height": raw_data.get("height"),
            "weight": raw_data.get("weight"),
        }
