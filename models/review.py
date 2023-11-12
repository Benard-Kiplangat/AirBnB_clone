#!/usr/bin/env python3
"""A class Review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review inherits from BaseModel
    attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
