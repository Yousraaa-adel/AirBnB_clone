#!/usr/bin/python3
""" This is the FileStorage class.
    Serializes instances to a JSON file and deserializes
    JSON file to instances.
"""
from datetime import datetime
import json
from models.base_model import BaseModel

class FileStorage():
    """ Representation of the FileStorage class. """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects. """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        obj_classname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_classname, obj.id)] = obj
        
    def delete(self, obj):
        """Deletes obj from __objects if it's inside."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
            self.save()  

    def save(self):
        """ Serializes __objects to the JSON file. """
        serialized_data = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict = obj.__dict__.copy()
            
            for attr, value in obj_dict.items():
                 if isinstance(value, datetime):
                    obj_dict[attr] = value.strftime('%Y-%m-%dT%H:%M:%S.%f') 
                                   
            serialized_data[key] = obj_dict

        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_data, file, indent=4)

    def reload(self):
        """ Deserializes the JSON file to __objects. """
           
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                
                for key, obj_dict in data.items():
                    class_name = key.split(".")[0]
                    cls = globals().get(class_name)
                    
                    if cls:
                        obj = cls(**obj_dict)
                        FileStorage.__objects[key] = obj
                        
        except FileNotFoundError:
            return

    