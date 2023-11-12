#!/usr/bin/env python3
"""A class City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City inherits from BaseModel
    attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
