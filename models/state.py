#!/usr/bin/python3
"""defines state class that inherits from the parent class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.

    Attribute:
        name (str): Name of state.
    """

    name = ""
