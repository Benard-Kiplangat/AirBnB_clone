#!/usr/bin/env python3
"""A class Amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity that inherits from BaseModel

    attributes:
        name <str>: name of the amenity
    """
    name = ""
