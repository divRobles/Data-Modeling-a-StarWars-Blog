import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    favoritos = relationship('Favorito', backref='user', lazy=True)


class Characters (Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gender = Column(String(50))
    eyesColor = Column(String(50))
    hairColor = Column(String(50))
    height = Column(Integer)
    skinColor = Column(String(50), nullable=False)
    favoritos = relationship('Favorito', backref='characters', lazy=True)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(String(250))
    terrain = Column(String(250), nullable=False)
    climate = Column(Integer)
    orbitalPeriod = Column(Integer)
    rotationPeriod = Column(Integer)
    diameter = Column(Integer)
    favoritos = relationship('Favorito', backref='planets', lazy=True)


class Favs(Base):
    __tablename__ = 'favs'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')