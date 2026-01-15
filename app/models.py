from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, JSON
from app.db import db


class Pokemon(db.Model):
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True)
    pokemon_id = Column(Integer, nullable=False, unique=True)
    name = Column(String, nullable=False)

    types = Column(JSON, nullable=False)
    stats = Column(JSON, nullable=False)
    abilities = Column(JSON, nullable=False)

    height = Column(Integer)
    weight = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Pokemon {self.name} ({self.pokemon_id})>"
