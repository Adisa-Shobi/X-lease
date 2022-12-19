#!/usr/bin/python3
'''
Class definition of Category objects
'''

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    '''
    Database mapping for categories table

    Properties:
        name: The name of the current category
        items: Relationship referencing all Items belonging to this category
    '''
    __tablename__ = 'categories'
    name = Column(String(50), nullable=False)
    items = relationship('Item', backref='category')
