#!/usr/bin/python3
''''''

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column,ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(50), nullable=False)
    country_id = Column(String(60), ForeignKey('countries.id'), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete, delete-orphan")