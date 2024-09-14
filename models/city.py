#!/usr/bin/python3
"""defines city class that inherits from the parent class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel, stores information about cities."""
    state_id = ""
    name = ""
