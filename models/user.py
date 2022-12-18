#!/usr/bin/python3
''''''

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String


class User(BaseModel, Base):
    __tablename__ = 'users'
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(5), nullable=False, unique=True)
    email = Column(String(124), nullable=True, unique=True)
    phone = Column(String(20), nullable=True)