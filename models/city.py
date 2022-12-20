#!/usr/bin/python3
'''
Definition for city objects
'''

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Float, Integer, String, ForeignKey


class City(BaseModel, Base):
    '''
    Database mapping for cities table

    Properties:
        name: The name of current city
        longitude: Longitudinal location of the city
        latitude: Latitudinal location of the city
        state_id: Foriegn key id of state said city is located in
    '''
    __tablename__ = 'cities'
    name = Column(String(50), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    longitude = Column(Float(), nullable=True)
    latitude = Column(Float(), nullable=True)
