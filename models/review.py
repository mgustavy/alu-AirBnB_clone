#!/usr/bin/python3
"""defines review class that inherits from the parent class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel, stores user reviews for places."""
    place_id = ""
    user_id = ""
    text = ""
