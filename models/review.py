#!/usr/bin/python
""" holds class Review"""
from models.item import Item
from .base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Representation of Review """
    __tablename__ = 'reviews'
    item_id = Column(String(60), ForeignKey('items.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
