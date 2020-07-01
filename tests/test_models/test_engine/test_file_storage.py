#!/usr/bin/python3
"""test_base_model
"""
import unittest
import pep8
import os
import json
from models.base_model import BaseModel
from models.__init__ import storage
from models import FileStorage


class TestBase(unittest.TestCase):
    """TextMaxInteger(unittest.TesCase)

    Args:
        unittest (Test): analysis of data
    """

    def test_pep8_conformance_base(self):
        """ test the pep8 style for module file_storage"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_base_test(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_1_instance_storage_exist(self):
        """ Check if methods exists """
        self.assertTrue(hasattr(storage, "__init__"))
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(hasattr(storage, "reload"))

    def test_2_storage_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(storage.__doc__)
        self.assertIsNotNone(storage.__init__.__doc__)
        self.assertIsNotNone(storage.all.__doc__)
        self.assertIsNotNone(storage.new.__doc__)
        self.assertIsNotNone(storage.save.__doc__)
        self.assertIsNotNone(storage.reload.__doc__)

    def test_3_arguments(self):
        """ test class arguments """
        with self.assertRaises(TypeError) as error:
            instance = FileStorage(1, 2, 3)
        messg = "object() takes no parameters"
        self.assertEqual(str(error.exception), messg)

    def test_4_attributes(self):
        """ tests class attributes"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_5_store_object(self):
        """tests objetct
        """
        test_1 = BaseModel()
        test_1.name = "Holberton"
        test_1.my_number = 89
        test_1.save()
        storage.reload()
        dic_obj = storage.all()
        self.assertTrue(dict, dic_obj)

    def test_6_save(self):
        """
        Testing the save method
        """
        test_1 = BaseModel()
        test_1.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_7_reload(self):
        """
        Test the reload file format dict
        """
        test_1 = BaseModel()
        test_1.save()
        test_1.name = "Erika"
        test_1.number = 1
        test_1.save()
        self.assertTrue(os.path.exists("file.json"))
        dic = {}
        with open('file.json', 'r') as fjson:
            dic = json.loads(fjson.read())
        test_1_key = test_1.__class__.__name__ + '.' + test_1.id
        self.assertDictEqual(test_1.to_dict(), dic[test_1_key])

    def test_8_new(self):
        """ Test the new in the object
        """
        test_1 = BaseModel()
        test_1.name = "Edison"
        test_2 = BaseModel()
        test_2.name = "Edison"
        id_tests_1 = test_1.id
        id_tests_2 = test_2.id
        self.assertFalse(id_tests_1 == id_tests_2)
