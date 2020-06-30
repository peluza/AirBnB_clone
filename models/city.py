#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """city

    Args:
        BaseModel (class):  the class is father

    """
    state_id = ""
    name = ""
