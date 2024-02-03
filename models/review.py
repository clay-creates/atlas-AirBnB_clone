#!/usr/bin/python3
"""
Module defining Review -> BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):

    place_id = "" # will be Place.id
    user_id = "" # will be User.id
    text = ""
