#!/usr/bin/env python3
"""A class that serializes instances to a JSON file and decerializes them back
"""
import json


class FileStorage:
    """A class that serializes and deserializes JSON file objects"""

    def __init__(self):
        """The init function to initialize the FileStorage class"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = "{}.{}".format(obj.__name__, obj.id)
            self.__objects[key] = obj
            self.save(self)

    def save(self):
        f = open(self.__file_path, "w")
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        json.dump(my_dict, f)
        f.close

    def reload(self):
        if self.__file_path:
            pass
        else:
            pass

