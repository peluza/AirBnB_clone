#!/usr/bin/python3
"""
    module : base_model
"""
import uuid
from datetime import datetime


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


# my_model = BaseModel()
# my_model.name = "Holberton"
# my_model.my_number = 89
# print(my_model.id)
# print(my_model)
# print(type(my_model.created_at))
# print("--")
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key,
#                                    type(my_model_json[key]), my_model_json[key]))

# print("--")
# my_new_model = BaseModel(**my_model_json)
# print(my_new_model.id)
# print(my_new_model)
# print(type(my_new_model.created_at))

# print("--")
# print(my_model is my_new_model)
