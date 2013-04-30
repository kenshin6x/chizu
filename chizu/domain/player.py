from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

from chizu.lib.base.domain import *


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nickname = Column(String)

    def fetchAll(self):
        return session.query(Player)

    def fetchById(self, id):
        return session.query(Player).filter(Player.id == id).first()

    def create(self, name, nickname):
        new_object = Player(name, nickname)

        session.add(new_object)
        session.commit()
