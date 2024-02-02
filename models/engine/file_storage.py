#!/usr/bin/python3
"""
This module contains the FileStorage class
"""
import json
from models.base_model import BaseModel


class FileStorage:

    def __init__(self):
        """
        Initialization of FileStorage
        """
        filename = "{}.json".format(self.__name__)
        __file_path = ...
        __objects = ...

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
