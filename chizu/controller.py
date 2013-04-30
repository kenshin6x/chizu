from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chizu.model import *

Session = sessionmaker(bind=engine)
session = Session()


class PlayerController(object):

    def getAll(self):
        return session.query(Player)

    def getById(self, id):
        return session.query(Player).filter(Player.id == id).first()

    def save(self, name, nickname):
        new_player = Player(name, nickname)
        session.add(new_player)
        session.commit()


class GameController(object):
    pass
