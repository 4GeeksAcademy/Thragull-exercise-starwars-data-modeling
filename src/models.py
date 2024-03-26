import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'), nullable=False)
    country= relationship(Country)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    name = Column(String(25), nullable=False)
    surname = Column(String(25), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(25), nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'), nullable=False)
    country= relationship(Country)
    address = Column(String(250), nullable=False)
    address2 = Column(String(250))
    address3 = Column(String(250))
    zipcode = Column(Integer, nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    city = relationship(City)
    phone = Column(Integer, nullable=False)
    registration = Column(DateTime, default=datetime.datetime.utcnow)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    population = Column(Integer, nullable=False)
    area = Column(Integer, nullable=False)
    suns =  Column(Integer)
    moons = Column(Integer)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    crew_capacity = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    width =  Column(Integer, nullable=False)
    moons = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), unique=True, nullable=False)
    planet= relationship(Planets)
    starship_id = Column(Integer, ForeignKey('starships.id'))
    starship = relationship(Starships)
    commands_id = Column(Integer, ForeignKey('starships.id'), unique=True)
    commands = relationship(Starships)
    
class Favourite_Characters(Base):
    __tablename__ = 'favourite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    character = relationship(Characters)

class Favourite_Starships(Base):
    __tablename__ = 'favourite_starships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    starship_id = Column(Integer, ForeignKey('starships.id'), nullable=False)
    starship = relationship(Starships)

class Favourite_Planets(Base):
    __tablename__ = 'favourite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    planet = relationship(Planets)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
