#!/usr/bin/python
'''
Definition of Country Class
'''

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship



class Country(BaseModel, Base):
    '''
    Database mapping of countries table

    Properties:
        name: The name of the current country
        states: Relationship referencing all states located in the current
                country
    '''
    __tablename__ = 'countries'
    name = Column(String(50), nullable=False)
    states = relationship('State', backref='country',
                          cascade="all, delete, delete-orphan")
