#!/usr/bin/python3
"""
    module: file_storage
"""
import json
import os
from ..base_model import BaseModel
from models.user import User


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
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as my_file:
                str_read = my_file.read()
            my_obj = json.loads(str_read)
            for k, v in my_obj.items():
                # class_name = k.split('.')[0]
                # self.__objects[k] = globals()[class_name](**v)
                # self.__objects[k] = globals()[k.split('.')[0]](**v)
                self.__objects[k] = BaseModel(**v)
