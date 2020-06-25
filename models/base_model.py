#!/usr/bin/python3
"""
    module : base_model
"""
import uuid
from datetime import datetime


class BaseModel:

    def __init__(self, id=0, created_at=0, updated_at=0):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        return str("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.update_at = datetime.today()

    def to_dict(self):
        dic = self.__dict__
        dic['updated_at'] = datetime.isoformat(self.updated_at)
        dic['created_at'] = datetime.isoformat(self.created_at)
        dic['__class__'] = self.__class__.__name__
        return dic
