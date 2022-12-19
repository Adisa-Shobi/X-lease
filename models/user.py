#!/usr/bin/python3
'''
Definition of User class
'''

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String


class User(BaseModel, Base):
    '''
    Database mapping of users table

    Properties:
        first_name: The first name of the user
        last_name: The last name of the user
        username: Users selected username
        email: Users email adderss
        phone: The phone number of the user
    '''
    __tablename__ = 'users'
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(124), nullable=True, unique=True)
    phone = Column(String(20), nullable=True)
