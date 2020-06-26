#!/usr/bin/python3
"""
    module: file_storage
"""
import json
import os
from ..base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        mydict = {}
        for k, v in self.__objects.items():
            mydict[k] = v.to_dict()
        with open(self.__file_path, mode='w+') as my_file:
            json.dump(mydict, my_file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as my_file:
                str_read = my_file.read()
            my_obj = json.loads(str_read)
            for k, v in my_obj.items():
                self.__objects[k] = globals()[k.split('.')[0]](**v)
