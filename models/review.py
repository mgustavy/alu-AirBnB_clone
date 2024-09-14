#!/usr/bin/python3
"""defines review class that inherits from the parent class"""
class Review(BaseModel):
    """Review class inherits from BaseModel, stores user reviews for places."""
    place_id = ""
    user_id = ""
    text = ""
