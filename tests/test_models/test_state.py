#!/usr/bin/python3
'''
Test classes for the State class
'''

import unittest
from models import state
from models.base_model import BaseModel
import inspect
State = state.State

class TestStateDocs(unittest.TestCase):
    '''
    Test to check documentation is present State Class
    '''
    @classmethod
    def setUpClass(cls):
        '''
        Sets up before for test mehtods
        '''
        cls.state_funcs = inspect.getmembers(State, inspect.isfunction)

    def test_state_module_docstring(self):
        '''
        Tests presence of docstring in user module
        '''
        self.assertIsNot(state.__doc__, None,
                            "'state.py' does not include a docsting")
        self.assertTrue(len(state.__doc__) >= 1)

    def test_state_class_docstring(self):
        '''
        Tests presence of docstring in state class
        '''
        self.assertIsNot(State.__doc__, None,
                            'state.State class is missing docstring')
        self.assertTrue(len(State.__doc__) >= 1,
                        'state.State docstring is an empty string')

    def test_state_func_docstrings(self):
        '''
        Tests that all functions/methods in the the State class have docstrings
        '''
        for func in self.state_funcs:
            self.assertIsNot(func[1].__doc__, None,
                             '{} does not contain a docstring'.format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            '{} contains an empty docstring'.format(func[0]))


class TestState(unittest.TestCase):
    '''
    Tests functionality of state class
    '''
    def test_is_subclass(self):
        '''
        Test ensures State is a subclass of BaseModel
        '''
        state = State()
        self.assertIsInstance(state, BaseModel,
                              'State is not an instance of Basemodel')
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))

    def test_attr_name(self):
        '''
        Tests first_name attribute presence and type
        '''
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, None)

    def test_attr_country_id(self):
        '''
        Tests country_id attribute presence and type
        '''
        state = State()
        self.assertTrue(hasattr(state, 'country_id'))
        self.assertEqual(state.country_id, None)

    def test_attr_cities(self):
        '''
        Tests cities attribute presence and type
        '''
        state = State()
        self.assertTrue(hasattr(state, 'cities'))
        self.assertIsInstance(state.cities, list)

    def test_mthd_dict(self):
        '''
        Confirms presence of all key-value pairs in dictionary
        '''
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertFalse('_sa_instance_state' in state_dict)
        for key in state.__dict__.keys():
            if key is not '_sa_instance_state':
                self.assertTrue(key in state_dict)
        self.assertTrue('__class__' in state_dict)

    def test_mthd_dict_values(self):
        '''
        Tests dictionary produced by to_dict() method
        '''
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(type(state_dict["created_at"]), str)
        self.assertEqual(type(state_dict["updated_at"]), str)
        self.assertEqual(state_dict["created_at"],
                         state.created_at.strftime(t_format))
        self.assertEqual(state_dict["updated_at"],
                         state.updated_at.strftime(t_format))

    def test_mthd_str(self):
        '''
        Tests custom __str__ method inherited from BaseModel
        '''
        state = State()
        test_string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(test_string, str(state))
