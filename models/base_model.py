#!/usr/bin/python3
""""Base class for Airbnb project"""

import uuid
from datetime import datetime

class BaseModel:
    """Defining the base class for the airbnb project"""
    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel atttributes"""
        self.id = str(uuid.uuid())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string reading of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.
                                     __name__, self.id, self.__dict__)

    def save(self):
        """This method upadtes the attribute (updated_at) with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """This method returns all values of the dictionary"""
        base_model_dict = self.__dict__.copy()
        base_model_dict['__class__'] = self.__class__.__name__
        base_model_dict['created_at'] = self.created_at.isoformat()
        base_model_dict['updated_at'] = self.updated_at.isoformat()
        return base_model_dict