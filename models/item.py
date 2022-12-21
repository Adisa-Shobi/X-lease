#!/usr/bin/python3
'''Definition of Item class
'''

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class Item(BaseModel, Base):
    '''
    Database mapping for items table

    Properties:
        name: The name of current item object
        price: The sale price of the item (incase of damage incurred)
        price_per_day: Price per day of leasing
        quantity: The number of similar items belonging to the same user
        description: A short description of the item
        category_id: Foreign key referncing the category the item belongs to
        owner_id: Foreign key referncing the user the item belongs to
        client_id: Foreign key referncing the user the item is currently
                   being leased to
    '''
    __tablename__ = 'items'
    name = Column(String(50), nullable=False)
    price = Column(Float(), nullable=False)
    price_per_day = Column(Float(), nullable=False)
    quantity = Column(Integer(), nullable=False)
    description = Column(Text(225), nullable=False)
    category_id = Column(String(60), ForeignKey('categories.id'))
    owner_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    leaser_id = Column(String(60), ForeignKey('users.id'), nullable=True,
                       default=None)
    owner = relationship('User', foreign_keys='Item.owner_id', backref='items')
    leaser = relationship('User', foreign_keys='Item.leaser_id',
                          backref='leased')
