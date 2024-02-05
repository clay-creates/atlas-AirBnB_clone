#!/usr/bin/python3
"""
This module contains the FileStorage class
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:

    def __init__(self):
        self.__objects = {}
        self.__file_path = "{}.json".format(self.__class__.__name__)

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets a new object in __objects with key
        """
        key = f"{obj['__class__']}.{obj['id']}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialized __objects to JSON file path
        """
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        with open(self.__file_path, 'r') as g:
            self.__objects = json.load(g)
