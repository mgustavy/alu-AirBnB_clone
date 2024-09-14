#!/usr/bin/python3
"""defines amenity class that inherits from the parent class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attribute:
        name (str): Name of amenity.
    """

    name = ""
