#!/usr/bin/python3
"""
Module defining the User -> BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):

    email = ""
    password = ""
    first_name = ""
    last_name = ""
