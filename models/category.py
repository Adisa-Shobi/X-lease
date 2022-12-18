#!/usr/bin/python3
''''''

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    __tablename__ = 'categories'
    name = Column(String(50), nullable=False)
    items = relationship('Item', backref='category')