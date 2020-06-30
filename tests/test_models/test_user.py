#!/usr/bin/python3
"""test_User
"""
import unittest
import pep8
import os
from models.user import User
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """TextMaxInteger(unittest.TesCase)

    Args:
        unittest (Test): analysis of data
    """

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_base_test(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_1_class(self):
        """ creates instance of User"""
        class_User = User()
        self.assertEqual(class_User.__class__.__name__, "User")

    def test_2_class_father(self):
        """ tests is subclass"""
        class_User = User()
        self.assertTrue(issubclass(class_User.__class__, BaseModel))

    def test_3_user(self):
        """ check if the user methods exists """
        user_1 = User()
        user_1.email = "1597@holbertonschool.com"
        user_1.password = "1234"
        user_1.first_name = "Edison"
        user_1.last_name = "Isaza"
        user_1.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(user_1.email, "1597@holbertonschool.com")
        self.assertTrue(user_1.password, "1234")
        self.assertTrue(user_1.first_name, "Edison")
        self.assertTrue(user_1.last_name, "Isaza")

    def test_4_file_User_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(User.__doc__)
