#!/usr/bin/python3
"""defines user class that inherits from the parent class"""

class User(BaseModel):
    """User class inherits from BaseModel, stores information about users."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""