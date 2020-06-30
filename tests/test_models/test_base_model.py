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

    def test_pep8_conformance_base_test(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_1_fiel_BaseModel_exist(self):
        """ Check if methods exists """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_2_file_BaseModel_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_3_class(self):
        """ creates instance of BaseModel"""
        class_BaseModel = BaseModel()
        self.assertEqual(class_BaseModel.__class__.__name__, "BaseModel")

    def test_4_date_time(self):
        """ check if the BaseModel create the datetime"""
        test_1 = BaseModel()
        test_date_1 = test_1.created_at
        test_2 = datetime.today()
        self.assertEqual(test_2.replace(microsecond=0),
                         test_date_1.replace(microsecond=0))

    def test_5_date_id(self):
        """ check if the BaseModel save the id diferent of the user"""
        test_1 = BaseModel()
        test_date_1 = test_1.id
        test_2 = BaseModel()
        test_date_2 = test_2.id
        self.assertFalse(test_date_1 == test_date_2)

    def test_6_date_save(self):
        """ check if the BaseModel update the datetime"""
        test_1 = BaseModel()
        test_date_1 = test_1.updated_at
        time.sleep(1)
        test_1.save()
        test_date_2 = test_1.updated_at
        self.assertTrue(os.path.exists('file.json'))
        self.assertNotEqual(test_date_1, test_date_2)
