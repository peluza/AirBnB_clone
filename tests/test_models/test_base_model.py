#!/usr/bin/python3
"""test_base_model
"""
import unittest
import time
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """TextMaxInteger(unittest.TesCase)

    Args:
        unittest (Test): analysis of data
    """

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_1_class(self):
        """ creates instance of BaseModel"""
        class_BaseModel = BaseModel()
        self.assertEqual(class_BaseModel.__class__.__name__, "BaseModel")

    def test_2_date_time(self):
        """ check if the BaseModel create the datetime"""
        test_1 = BaseModel()
        test_date_1 = test_1.created_at
        test_2 = datetime.today()
        self.assertEqual(test_2.replace(microsecond=0),
                          test_date_1.replace(microsecond=0))

    def test_3_date_id(self):
        """ check if the BaseModel save the id diferent of the user"""
        test_1 = BaseModel()
        test_date_1 = test_1.id
        test_2 = BaseModel()
        test_date_2 = test_2.id
        self.assertFalse(test_date_1 == test_date_2)

    def test_4_date_save(self):
        """ check if the BaseModel update the datetime"""
        test_1 = BaseModel()
        test_date_1 = test_1.updated_at
        time.sleep(1)
        test_1.save()
        test_date_2 = test_1.updated_at
        self.assertTrue(os.path.exists('file.json'))
        self.assertNotEqual(test_date_1, test_date_2)
