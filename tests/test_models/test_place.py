#!/usr/bin/python3
"""test_Place
"""
import unittest
import pep8
import os
from models.place import Place
from models.base_model import BaseModel

class TestBase(unittest.TestCase):
    """TextMaxInteger(unittest.TesCase)

    Args:
        unittest (Test): analysis of data
    """

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_1_class(self):
        """ creates instance of Place"""
        class_Place = Place()
        self.assertEqual(class_Place.__class__.__name__, "Place")

    def test_2_class_father(self):
        """ tests is subclass"""
        class_Place = Place()
        self.assertTrue(issubclass(class_Place.__class__, BaseModel))

    def test_3_Place(self):
        """ check if the Place methods exists """
        Place_1 = Place()
        Place_1.city_id = "LA"
        Place_1.user_id = "12340858294"
        Place_1.name = "Erika Osorio"
        Place_1.description = "the area has a green area"
        Place_1.number_rooms = 4
        Place_1.number_bathrooms = 5
        Place_1.max_guest = 2
        Place_1.price_by_night = 123.304
        Place_1.latitude = 34.05223
        Place_1.longitude = -118.24368
        Place_1.amenity_ids = "452342"
        Place_1.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertTrue(Place_1.city_id, "CA")
        self.assertTrue(Place_1.user_id, "12340858294")
        self.assertTrue(Place_1.name, "Erika Osorio")
        self.assertTrue(Place_1.description, "the area has a green area")
        self.assertTrue(Place_1.number_rooms, 4)
        self.assertTrue(Place_1.number_bathrooms, 5)
        self.assertTrue(Place_1.max_guest, 2)
        self.assertTrue(Place_1.price_by_night, 123.304)
        self.assertTrue(Place_1.latitude, 34.05223)
        self.assertTrue(Place_1.longitude, -118.24368)
        self.assertTrue(Place_1.amenity_ids, "452342")
