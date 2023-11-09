#!/usr/bin/env python3
"""Class BaseModel that instatiates the Cmd class for our console"""
import cmd
import uuid
import datetime


class BaseModel(cmd.Cmd):
    """BaseModel class for the console of our AirBnB project
        attributes (class): Cmd module
    """
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now().isoformat()
    updated_at = datetime.datetime.now().isoformat()

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
                if "id" not in kwargs.keys():
                    setattr(self, "id", str(uuid.uuid4()))
                time = datetime.datetime.now().isoformat()
                if "created_at" not in kwargs.keys():
                    setattr(self, "created_at", time)
                if "updated_at" not in kwargs.keys():
                    setattr(self, "updated_at", time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        return "[{}] ({}) <{}>".format(self.name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        return my_dict
