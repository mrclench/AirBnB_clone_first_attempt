#!/usr/bin/python3
"""File Storage"""

import json
import os
import datetime


class FileStorage:
    """File storage class for serialization and deserialization of objects"""
    __file_path = "file.json"
    __objects = {}
    instances = {}
    classes = {}

    def __init__(self, storage=None):
        """Initialize FileStorage instance"""
        self.reload()

#        self.storage = FileStorage()
#        self.storage.reload()
#        FileStorage.instances[type(self).__name__] = self

#    @property
    def all(self):
        """returns the dictionary _objects"""
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with the key <obj class name>.id"""
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        """could have used 'key' instead of 'obj_key' - still works"""
        self.__objects[obj_key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value.get('__class__')
                    if class_name and class_name in globals():
                        obj_instance = globals()[class_name](**value)
                        self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
