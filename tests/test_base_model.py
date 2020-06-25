#!/usr/bin/python3
"""test_base_model
"""
import unittest
import datetime
import pep8
from models/base_model import BaseModel


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

    def date_time(self):
        date = self.BaseModel.created_at
        self.assertAlmostEqual(datetime.datetime.today(), date)
