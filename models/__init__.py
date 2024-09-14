#!/usr/bin/python3
"""The __init__ method for models directory"""

from models.engine.file_storage import FileStorage

#initialization of the storage engine
storage = FileStorage()

#Reloads storage engine to load objects from the JSON file (if any)
storage.reload()