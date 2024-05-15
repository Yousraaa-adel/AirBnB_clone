#!/usr/bin/python3
""" The BaseModel class.
    Defines all common attributes/methods for other classes.
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """ Representation of the base model. """

    def __init__(self, *args, **kwargs):
        """ ntitializes the BaseModel class.
        Args:
            id (int): identity of the class.
            created_at (datetime): time created at.
            updated_at (datetime): time updated at.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key,
                                datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

        if not hasattr(self, "id"):
            self.id = str(uuid4())
        if not hasattr(self, "created_at"):
            self.created_at = datetime.now()
        if not hasattr(self, "updated_at"):
            self.updated_at = datetime.now()

    def save(self):
        """ Updates the time stamp. """
        updated_time = self.updated_at = datetime.now()
        models.storage.save()

        return updated_time

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of
            __dict__ of the instance.
        """
        dictionary = self.__dict__

        dictionary["__class__"] = self.__class__.__name__
        if isinstance(self.created_at, datetime):
            dictionary["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        if isinstance(self.updated_at, datetime):
            dictionary["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return dictionary

    def __str__(self):
        """ Overrides the __str__ method. """
        
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
