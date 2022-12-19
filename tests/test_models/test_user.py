#!/usr/bin/python3
'''
Test classes for the User class
'''

import unittest
from models import user
from models.base_model import BaseModel
import inspect
User = user.User

class TestUserDocs(unittest.TestCase):
    '''
    Test to check documentation is present User Class
    '''
    @classmethod
    def setUpClass(cls):
        '''
        Sets up before for test mehtods
        '''
        cls.user_funcs = inspect.getmembers(User, inspect.isfunction)

    def test_user_module_docstring(self):
        '''
        Tests presence of docstring in user module
        '''
        self.assertIsNot(user.__doc__, None,
                            "'user.py' does not include a docsting")
        self.assertTrue(len(user.__doc__) >= 1)

    def test_user_class_docstring(self):
        '''
        Tests presence of docstring in user class
        '''
        self.assertIsNot(User.__doc__, None,
                            'user.User class is missing docstring')
        self.assertTrue(len(User.__doc__) >= 1,
                        'user.User docstring is an empty string')

    def test_user_func_docstrings(self):
        '''
        Tests that all functions/methods in the the User class have docstrings
        '''
        for func in self.user_funcs:
            self.assertIsNot(func[1].__doc__, None,
                             '{} does not contain a docstring'.format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            '{} contains an empty docstring'.format(func[0]))


class TestUser(unittest.TestCase):
    '''
    Tests functionality of user class
    '''
    def test_is_subclass(self):
        '''
        Test ensures User is a subclass of BaseModel
        '''
        user = User()
        self.assertIsInstance(user, BaseModel,
                              'User is not an instance of Basemodel')
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))

    def test_attr_first_name(self):
        '''
        Tests first_name attribute presence and type
        '''
        user = User()
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual(user.first_name, None)

    def test_attr_last_name(self):
        '''
        Tests last_name attribute presence and type
        '''
        user = User()
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.last_name, None)

    def test_attr_email(self):
        '''
        Tests email attribute presence and type
        '''
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual(user.email, None)

    def test_attr_phone(self):
        '''
        Tests phone attribute presence and type
        '''
        user = User()
        self.assertTrue(hasattr(user, 'phone'))
        self.assertEqual(user.phone, None)

    def test_mthd_dict(self):
        '''
        Confirms presence of all key-value pairs in dictionary
        '''
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertFalse('_sa_instance_state' in user_dict)
        for key in user.__dict__.keys():
            if key is not '_sa_instance_state':
                self.assertTrue(key in user_dict)
        self.assertTrue('__class__' in user_dict)

    def test_mthd_dict_values(self):
        '''
        Tests dictionary produced by to_dict() method
        '''
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(type(user_dict["created_at"]), str)
        self.assertEqual(type(user_dict["updated_at"]), str)
        self.assertEqual(user_dict["created_at"],
                         user.created_at.strftime(t_format))
        self.assertEqual(user_dict["updated_at"],
                         user.updated_at.strftime(t_format))

    def test_mthd_str(self):
        '''
        Tests custom __str__ method inherited from BaseModel
        '''
        user = User()
        test_string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(test_string, str(user))
