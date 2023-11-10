#!/usr/bin/env python3
"""A class that serializes instances to a JSON file and decerializes them back
"""


class FileStorage:
    """A class that serializes and deserializes JSON file objects"""

    def __init__(self):
        """The init function to initialize the FileStorage class"""
        self.__file_path = ""
        self.__objects = ()

    def all(self):
        return self.__objects

    def new(self, obj):
        pass

    def save(self):
        pass

    def reload(self):
        if self.__file_path:
            pass
        else:
            pass

