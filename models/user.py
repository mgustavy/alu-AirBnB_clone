#!/usr/bin/python3
"""defines user class that inherits from the parent class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel, stores information about users."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
