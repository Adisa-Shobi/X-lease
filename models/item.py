#!/usr/bin/python3
''''''

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text


class Item(BaseModel, Base):
    __tablename__ = 'items'
    name = Column(String(50), nullable=False)
    price = Column(Float(), nullable=False)
    price_per_day = Column(Float(), nullable=False)
    quantity = Column(Integer(), nullable=False)
    description = Column(Text(225), nullable=False)
    category_id = Column(String(60), ForeignKey('categories.id'))
    item_owner = Column(String(60), ForeignKey('users.id'), nullable=False)
    leased_to = Column(String(60), ForeignKey('users.id'), nullable=True)