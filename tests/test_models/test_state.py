#!/usr/bin/python3
"""test_State
"""
import unittest
import pep8
import os
from models.state import State
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """TextMaxInteger(unittest.TesCase)

    Args:
        unittest (Test): analysis of data
    """

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_base_test(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_1_class(self):
        """ creates instance of State"""
        class_State = State()
        self.assertEqual(class_State.__class__.__name__, "State")

    def test_2_class_father(self):
        """ tests is subclass"""
        class_State = State()
        self.assertTrue(issubclass(class_State.__class__, BaseModel))

    def test_3_State(self):
        """ check if the State methods exists """
        State_1 = State()
        State_1.name = "California"
        State_1.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(State_1.name, "California")

    def test_4_file_State_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(State.__doc__)
