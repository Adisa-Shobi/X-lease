#!/usr/bin/python3
'''
Definition of State class
'''

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column,ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    '''
    Database mapping for the states table

    Properties:
        name: The name of the satae
        cities: Related to the cities table, property for
                referenceing all cities under state
        country_id: Foreign key id of country said state belongs to
    '''
    __tablename__ = 'states'
    name = Column(String(50), nullable=False)
    country_id = Column(String(60), ForeignKey('countries.id'), nullable=False)
    cities = relationship('City', backref='state',
                          cascade="all, delete, delete-orphan")
