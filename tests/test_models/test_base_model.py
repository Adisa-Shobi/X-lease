#!/usr/bin/python3
'''
Test for base model
'''
from models import base_model
import unittest
import inspect
BaseModel = base_model.BaseModel

class TestBaseModel(unittest.TestCase):
    '''
    Test cases for Base model defines
    '''
    @classmethod
    def setUpClass(cls):
        '''
        Sets up before for test mehtods
        '''
        cls.base_model_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_base_model_module_docstring(self):
        '''
        Tests presence of docstring in base_model module
        '''
        self.assertIsNot(base_model.__doc__, None,
                            "'base_model.py' does not include a docsting")
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_base_model_class_docstring(self):
        '''
        Tests presence of docstring in base_model class
        '''
        self.assertIsNot(BaseModel.__doc__, None,
                            'base_model.BaseModel class is missing docstring')
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        'base_model.BaseModel docstring is an empty string')

    def test_base_model_func_docstrings(self):
        '''
        Tests that all functions/methods in the the BaseModel class have docstrings
        '''
        for func in self.base_model_funcs:
            self.assertIsNot(func[1].__doc__, None,
                             '{} does not contain a docstring'.format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            '{} contains an empty docstring'.format(func[0]))
