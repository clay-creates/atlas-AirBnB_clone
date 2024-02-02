#!/usr/bin/python3
"""
This module defines the BaseModel class, parent for all other classes
"""
import datetime
import uuid


class BaseModel:

    def __init__(self):
        """
        Initialization for BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    @property
    def save(self):
        """
        Updates updated_at with current datetime
        """
        self.updated_at = datetime.datetime.now()


    @property
    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of instance
        """
        return self.__dict__