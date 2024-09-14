#!/usr/bin/python3
"""defines user class that inherits from the parent class"""
from models.base_model import BaseModel

"""User class inherits from BaseModel."""
class User(BaseModel):
    
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
