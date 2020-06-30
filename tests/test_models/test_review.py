#!/usr/bin/python3
"""test_Review
"""
import unittest
import pep8
import os
from models.review import Review
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """TextMaxInteger(unittest.TesCase)

    Args:
        unittest (Test): analysis of data
    """

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_base_test(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_1_class(self):
        """ creates instance of Review"""
        class_Review = Review()
        self.assertEqual(class_Review.__class__.__name__, "Review")

    def test_2_class_father(self):
        """ tests is subclass"""
        class_Review = Review()
        self.assertTrue(issubclass(class_Review.__class__, BaseModel))

    def test_3_Review(self):
        """ check if the Review methods exists """
        Review_1 = Review()
        Review_1.place_id = "403956"
        Review_1.user_id = "540982345"
        Review_1.text = "Erika Osorio"
        Review_1.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(Review_1.place_id, "403956")
        self.assertTrue(Review_1.user_id, "540982345")
        self.assertTrue(Review_1.text, "Erika Osorio")

    def test_4_file_Review_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(Review.__doc__)
