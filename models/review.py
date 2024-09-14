#!/usr/bin/python3
"""defines review class that inherits from the parent class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): Text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
