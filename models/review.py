#!/usr/bin/python
""" holds class Review"""
from models.item import Item
from .base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """
    Database mapping of the reviews table

    Properties:
        item_id: Foreign key referencing the item described by current review
        user_id: Foreign key referencing current reviews author
        text: The review content
    """
    __tablename__ = 'reviews'
    item_id = Column(String(60), ForeignKey('items.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
    item = relationship('Item', backref='reviews')
    user = relationship('User', backref='reviews')
