#!/usr/bin/python3
"""
    module : base_model
"""
import uuid
from datetime import datetime
import models

class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs is not None and kwargs != {}:
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
        return str("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        dic = self.__dict__
        dic['updated_at'] = datetime.isoformat(self.updated_at)
        dic['created_at'] = datetime.isoformat(self.created_at)
        dic['__class__'] = self.__class__.__name__
        return dic
