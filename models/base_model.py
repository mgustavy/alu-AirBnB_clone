import uuid
from datetime import datetime

class BaseModel:
    """defines all common attributes/methods for child classes"""
    def __init__(self,*args,**kwargs):
        """initialisation of the basemodel"""
        if kwargs:
            for key,value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.isfromoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            updated_at = self.created_at
    
    def save(self):
        """changes the updated_at to the current time"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """returns a dictionary string representation of the instance"""
        instance_dict = self.__dict__.copy()
        # Convert created_at and updated_at to ISO 8601 format strings
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        return instance_dict