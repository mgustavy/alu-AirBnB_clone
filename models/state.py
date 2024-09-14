#!/usr/bin/python3
"""defines state class that inherits from the parent class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class inherits from BaseModel, stores information about states/regions."""
    name = ""
