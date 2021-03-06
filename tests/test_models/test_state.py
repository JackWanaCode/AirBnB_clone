#!/usr/bin/python3
""" Test cases for user class
"""
import unittest
from models.state import State
from models import storage
import os
import json


def setUpModule():
    """ setup
    """
    if os.path.isfile("file.json"):
        os.remove("file.json")
    storage._FileStorage__objects.clear()


def tearDownModule():
    """ teardown
    """
    if os.path.isfile("file.json"):
        os.remove("file.json")


class TestState(unittest.TestCase):
    """ Test User class
    """
    name = "file.json"

    def test_class_attributes(self):
        """ Test User class attributes """
        check = 0
        my_state = State()
        """
        Test keys in User dictionary
        """
        self.assertTrue(sorted(list(my_state.__dict__.keys())) ==
                        ['created_at', 'id', 'updated_at'], True)
        """
        Test for class attributes in User
        """
        self.assertEqual(my_state.name, '')
        my_state.name = "California"
        my_state.save()
        self.assertEqual(my_state.name, "California")
        """
        Test file.json store the object just created
        """
        if os.path.isfile(TestState.name):
            with open(TestState.name, 'r') as f:
                string = f.read()
                dic = json.loads(string)
                for key, value in dic.items():
                    if key.split('.')[1] == my_state.id:
                        check = 1
                        break
        self.assertEqual(check, 1)

if __name__ == '__main__':
    unittest.main()
