#!/usr/bin/python3
"""File Storage"""

import json
import os
import datetime


class FileStorage:
    """File storage class for serialization and deserialization of objects"""
    __file_path = "data_storage.json"
    __objects = {}

    def all(self):
        """returns the dictionary _objects"""
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with the key <obj class name>.id"""
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        """could have used 'key' instead of 'obj_key' - still works"""
        self.__objects[obj_key] = obj

    def save(self):
        """serializes _objects to a json file """
        with open('data_storage.json', 'w', encoding='utf-8') as file:
            json.dump(self.__objects, file, default=lambda o: o.__dict__, indent=4)

    def reload(self):
        """This instance method deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                self.__objects = json.load(file)
        else:
            {}
