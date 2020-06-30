#!/usr/bin/python3
"""test_amenity
"""
import unittest
import pep8
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """TextMaxInteger(unittest.TesCase)

    Args:
        unittest (Test): analysis of data
    """

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_base_test(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_1_class(self):
        """ creates instance of amenity"""
        class_Amenity = Amenity()
        self.assertEqual(class_Amenity.__class__.__name__, "Amenity")

    def test_2_class_father(self):
        """ tests is subclass"""
        class_Amenity = Amenity()
        self.assertTrue(issubclass(class_Amenity.__class__, BaseModel))

    def test_3_Amenity(self):
        """ check if the Amenity methods exists """
        Amenity_1 = Amenity()
        Amenity_1.name = "the greenzone"
        Amenity_1.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(Amenity_1.name, "the greenzone")

    def test_4_file_Amenity_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(Amenity.__doc__)
