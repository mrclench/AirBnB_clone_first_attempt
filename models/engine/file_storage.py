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
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    class_ = globals()[class_name]
                    obj = class_(**obj_dict)
                    self.__objects[key] = obj
                    self.classes[class_name] = class_
        except FileNotFoundError:
            pass



