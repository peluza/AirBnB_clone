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

    def test_storage(self):
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        print(my_model)
