#!/usr/bin/python3
"""
this module defines a file storage class that handles
serialization and deserialization processes
"""

import json
class FileStorage:
    """Handles storing and loading data from a file."""
    
    #path to the JSON file
    __file_path_= "file.json"
    
    #stores ID's for all objects
    __objects = {}

    def all(self):
        """returns all objects stored in _objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """creates new object to the dictionary"""
        self._objects[obj.id] = obj

    def save(self):
        """serializes an object to a JSON file"""
        serialized_objects = {obj_id: obj.to_dict() for obj_id, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path_, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """deserializes the JSON file to an object"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for obj_id, obj_data in obj_dict.items():
                    class_name = obj_data['__class__']
                    #Dynamically create the class instance from the class name (BaseModel or subclasses)
                    obj_class = globals()[class_name]
                    self.__objects[obj_id] = obj_class.from_dict(obj_data)
        # If the file doesn't exist yet, do nothing
        except FileNotFoundError:
            pass 