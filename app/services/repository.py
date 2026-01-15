from typing import Optional
from app.db import db
from app.models import Pokemon


class PokemonRepository:
    @staticmethod
    def get_by_pokemon_id(pokemon_id: int) -> Optional[Pokemon]:
        return Pokemon.query.filter_by(pokemon_id=pokemon_id).first()

    @staticmethod
    def create(pokemon_data: dict) -> Pokemon:
        pokemon = Pokemon(**pokemon_data)
        db.session.add(pokemon)
        db.session.commit()
        return pokemon

    @staticmethod
    def get_all():
        return Pokemon.query.all()

    def delete_by_name(name: str) -> bool:
        pokemon = Pokemon.query.filter_by(name=name.lower()).first()
        if not pokemon:
            return False

        db.session.delete(pokemon)
        db.session.commit()
        return True
