#!/usr/bin/python3
"""
    module: file_storage
"""
import json
import os
from ..base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State

dic_of_class = {
    "BaseModel": BaseModel, "City": City,
    "Place": Place, "State": State,
    "User": User, "Review": Review,
    "Amenity": Amenity
}


class FileStorage:
    """ class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all

        Returns:
            [dic]: variable privade __objetcs
        """
        return self.__objects

    def new(self, obj):
        """new

        Args:
            obj (dic): the objects is diccionary
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """save elements in the file.json
        """
        mydict = {}
        for k, v in self.__objects.items():
            mydict[k] = v.to_dict()
        with open(self.__file_path, mode='w+') as my_file:
            json.dump(mydict, my_file)

    def reload(self):
        """reload elements in the file.json
        """
        classes = {}

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as my_file:
                str_read = my_file.read()
            my_obj = json.loads(str_read)
            for k, v in my_obj.items():
                which_cls = k.split('.')[0]
                the_class = dic_of_class[which_cls]
                self.__objects[k] = the_class(**v)
                # eval(class_name(**v))
                # self.__objects[k] = globals()[class_name](**v)
                # self.__objects[k] = globals()[k.split('.')[0]](**v)
                # self.__objects[k] = BaseModel(**v)
