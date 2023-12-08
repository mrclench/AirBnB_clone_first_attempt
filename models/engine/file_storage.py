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
