#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """Review

    Args:
        BaseModel (class):  the class is father
    """
    place_id = ""
    user_id = ""
    text = ""
