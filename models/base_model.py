#!/usr/bin/env python3
"""Class BaseModel that instatiates the Cmd class for our console"""
import cmd
import uuid
import datetime


class BaseModel(cmd.Cmd):
    """BaseModel class for the console of our AirBnB project
        attributes (class): Cmd module
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()
        if **kwargs is not None:
            print(self.id)
        else:
            print(self.created_at)

    def __str__(self):
        return "[{}] ({}) <{}>".format(self.name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        return dict(self.__dict__)
