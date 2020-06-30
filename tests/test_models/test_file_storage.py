#!/usr/bin/python3
"""test_base_model
"""
import unittest
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
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_base_test(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_1_fiel_storage_exist(self):
        """ Check if methods exists """
        self.assertTrue(hasattr(storage, "__init__"))
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(hasattr(storage, "reload"))

    def test_2_file_storage_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(storage.__doc__)
        self.assertIsNotNone(storage.__init__.__doc__)
        self.assertIsNotNone(storage.all.__doc__)
        self.assertIsNotNone(storage.new.__doc__)
        self.assertIsNotNone(storage.save.__doc__)
        self.assertIsNotNone(storage.reload.__doc__)
