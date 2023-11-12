#!/usr/bin/env python3
"""A class User that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class State inherits from BaseModel
    attributes:
        name: string - empty string
    """
    name = ""
