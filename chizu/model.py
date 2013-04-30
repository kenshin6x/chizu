from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///chizu.db', echo=True)
Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nickname = Column(String)

    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname


Base.metadata.create_all(engine)
