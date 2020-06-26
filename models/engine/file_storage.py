#!/usr/bin/python3
"""
    module: file_storage
"""
import json, os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        filename = FileStorage.__file_path
        with open(filename, mode="w", encoding="utf-8") as my_file:
            dict_storage_obj = {
                   key: value.to_dict()
                for (key,value) in FileStorage.__objects.items()
            }
            json.dump(dict_storage_obj, my_file)

    def reload(self):
        filename = FileStorage.__file_path
        try:
            with open(filename, mode="r", encoding="utf-8") as my_file:
                FileStorage.__objects = json.load(my_file)
        except:
            pass
