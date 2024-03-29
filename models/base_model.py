#!/usr/bin/python3
""""Base class for Airbnb project"""

import json
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defining the base class for the airbnb project"""
    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel attributes"""

        if kwargs:
            """Collects the attributes with keys from kwargs"""
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)

        else:
            """Recreate new instances for attributes"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string reading of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.
                                     __qualname__, self.id, self.__dict__)

    def __repr__(self):
        """returns string function"""
        return self.__str__()

    def save(self):
        """This method updates the attribute (updated_at) with current datetime
        and serializes __objects into a JSON file (path: __file_path)"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This method converts attributes of an instance into a dictionary"""
        base_model_dict = self.__dict__.copy()
        base_model_dict['__class__'] = self.__class__.__qualname__
        base_model_dict['created_at'] = self.created_at.isoformat()
        base_model_dict['updated_at'] = self.updated_at.isoformat()
        return base_model_dict

    def reload(self):
        """Deserialize the JSON file to __objects"""
        storage.reload()
