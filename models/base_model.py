#!/usr/bin/python3
"""
    module : base_model
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
        BaseModel main class
        set the value of a new instance
        or instance a class from a dictionary of an obj previous
        created
    """

    def __init__(self, *args, **kwargs):
        """__init__ Constructor

        *args
        **kwargs: (Dictionary of the object)
        """
        if kwargs is not None and kwargs != {}:
            self.__dict__ = kwargs
            if "__class__" in self.__dict__:
                del self.__dict__["__class__"]
            self.id = kwargs['id']
            self.created_at = datetime.strptime(
                kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(
                kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """__str__ No official repre of an object

        creates a string representation of the class name, the id and
        its dictionary

        Returns:
            str: the representation NO OFICIAL of the object
        """
        return str("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """save Updates the datetime of the instance

           storage with the class Filestorage calls save method
           to storage in the Json.file

        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """to_dict dictionary of the object

        Is a copy of the dictionary and repace in a isoformat the
        update time and the created time.
        Returns:
            dict: new dictionary of the object
        """
        dic = self.__dict__.copy()
        dic['updated_at'] = datetime.isoformat(self.updated_at)
        dic['created_at'] = datetime.isoformat(self.created_at)
        dic['__class__'] = self.__class__.__name__
        return dic
