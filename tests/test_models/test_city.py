#!/usr/bin/python3
"""test_City
"""
import unittest
import pep8
import os
from models.city import City
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """TextMaxInteger(unittest.TesCase)

    Args:
        unittest (Test): analysis of data
    """

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_base_test(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_1_class(self):
        """ creates instance of City"""
        class_City = City()
        self.assertEqual(class_City.__class__.__name__, "City")

    def test_2_class_father(self):
        """ tests is subclass"""
        class_City = City()
        self.assertTrue(issubclass(class_City.__class__, BaseModel))

    def test_3_City(self):
        """ check if the City methods exists """
        City_1 = City()
        City_1.state_id = "CA"
        City_1.name = "Los Angeles"
        City_1.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(City_1.state_id, "CA")
        self.assertTrue(City_1.name, "Los Angeles")

    def test_4_file_City_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(City.__doc__)
