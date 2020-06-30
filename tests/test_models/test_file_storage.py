#!/usr/bin/python3
"""test_base_model
"""
import unittest
import time
from datetime import datetime
import pep8
from models.base_model import BaseModel
from models.__init__ import storage


class TestBase(unittest.TestCase):
    """TextMaxInteger(unittest.TesCase)

    Args:
        unittest (Test): analysis of data
    """

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storange.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
