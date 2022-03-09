#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestState(unittest.TestCase):
     """this will test the State class"""

     @classmethod
     def setUpClass(cls):
         """set up for test"""
         cls.state = State()
         cls.state.name = "CA"
