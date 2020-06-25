#!/usr/bin/python3
"""test_base_model
"""
import unittest
import time
from datetime import datetime
import pep8
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

    def test_1_date_time(self):
        test_1 = BaseModel()
        test_date_1 = test_1.created_at
        test_2 = datetime.today()
        self.assertEqual(test_2.replace(microsecond=0),
                          test_date_1.replace(microsecond=0))

    def test_2_date_id(self):
        test_1 = BaseModel()
        test_date_1 = test_1.id
        test_2 = BaseModel()
        test_date_2 = test_2.id
        self.assertFalse(test_date_1 == test_date_2)

    def test_3_date_save(self):
        test_1 = BaseModel()
        test_date_1 = test_1.updated_at
        time.sleep(1)
        test_1.save()
        test_date_2 = test_1.updated_at
        self.assertNotEqual(test_date_1, test_date_2)

    def test_4_dict(self):
        test_1 = BaseModel()
        dic = test_1.to_dict()
        self.assertEqual(
            dic,
            {'created_at': test_1.created_at, 'updated_at': test_1.updated_at, 'id': test_1.id, '__class__': test_1.__class__.__name__})
