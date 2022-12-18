#!/usr/bin/python3
''''''

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Float, Integer, String, ForeignKey


class City(BaseModel, Base):
    __tablename__ = 'cities'
    name = Column(String(50), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'))
    longitude = Column(Float(), nullable=True)
    latitude = Column(Float(), nullable=True)

    
