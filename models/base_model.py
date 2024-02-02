#!/usr/bin/python3
"""
This module defines the BaseModel class, parent for all other classes
"""
from datetime import datetime
import uuid

class BaseModel:

    def __init__(self):
        """
        Initialization for BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates updated_at with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of instance
        """
        self.__dict__['__class__']: self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__