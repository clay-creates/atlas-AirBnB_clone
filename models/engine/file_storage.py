#!/usr/bin/python3
"""
This module contains the FileStorage class
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:

    __file_path = "{}.json".format(__name__)
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets a new object in __objects with key
        """
        ...

    def save(self):
        """
        Serialized __objects to JSON file path
        """
        ...

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        ...
