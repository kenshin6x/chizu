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

    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname

    @staticmethod
    def fetchAll():
        return session.query(Player)

    @staticmethod
    def fetchById(id):
        return session.query(Player).filter(Player.id == id).first()

    def save(self):
        session.add(self)
        session.commit()

    def update(self):
        session.update(self)
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()
