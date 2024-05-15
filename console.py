#!/usr/bin/python3
""" This is the console module.
    The entry point of the command interpreter.
"""
from cmd import Cmd
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(Cmd):
    """Defines the AirBnb command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """   
    
    prompt = "(hbnb) "
    doc_header = "Documented commands"
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State
        } 
    
    @staticmethod        
    def check_exist_class(args = []):
        """ check class  if it exists """
        
        if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return 
        else:
            if len(args) == 1: 
                print("** instance id missing **")
                return
     
    @staticmethod       
    def check_exist_id(args= [], instance_key =None, all_classes=None):
        """ check id if it exists """
        if args[0] in HBNBCommand.__classes and len(args) > 1:
            if instance_key not in all_classes:
                        print("** no instance found **")
                        return -1
            else:
                    if len(args) == 2:
                        print("** attribute name missing **")
                        return
                    
                    elif len(args) == 3:
                        print("** value missing **")
                        return                
                            
                            
    def do_quit(self, line):
        """Quit command to exit the program."""
        return True
    
    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("Goodbye!")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create (self, line):
        """ Usage: create <class>
        Create a new class instance and print its id.
        """
        if not line:
            print("** class name missing **")
            return

        elif line not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        else:
            b1 = HBNBCommand.__classes[line]()
            storage.save()
            print(b1.id)
            
    def do_show(self, line):
        """ Prints the string representation
        of an instance based on the class name and id
        """
        all_classes = storage.all()
        args = line.split() 
        if len(args) == 0:
            print("** class name missing **")
            return
        
        elif len(args) == 1:
            HBNBCommand.check_exist_class(args)
            
        elif len(args) == 2:
            HBNBCommand.check_exist_class(args)
            instance_key = f"{args[0]}.{args[1]}"
            
            if args[0] in HBNBCommand.__classes and len(args) > 1:
                if instance_key not in all_classes:
                        print("** no instance found **")
                        return 
                else:
                    instance = all_classes[instance_key]
                    print(instance)

    def do_destroy(self, line):
        """  Delete Instance from json """
        all_classes = storage.all()
        args = line.split()
        
        if len(args) == 0:
            print("** class name missing **")
            return
        
        elif len(args) == 1:
            HBNBCommand.check_exist_class(args)
        
        elif len(args) == 2:
            HBNBCommand.check_exist_class(args)
            instance_key = f"{args[0]}.{args[1]}"
            if args[0] in HBNBCommand.__classes and len(args) > 1:
                if instance_key not in all_classes:
                        print("** no instance found **")
                        return 
                else:
                    storage.delete(all_classes[instance_key])
                    print("Deleted Successfully")

    def do_all(self, line):
        """ Prints all string representation of all instances
            based or not on the class name.
        """
        all_classes = storage.all()

        if line:
            if line not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            else:
                for key, value in all_classes.items():
                    new_key = key.split(".")
                    if new_key[0] == line:
                        value = all_classes[key]
                        print(value)
                    else:
                        print("No")

        else:
            for key, value in all_classes.items():
                value = all_classes[key]
                print(value)

    def do_update(self, line):
        """ Updates an instance based on the class name and id
            by adding or updating attribute
            (save the change into the JSON file). 
        """
        all_classes = storage.all()
        args = line.split() 
        
        if len(args) == 0 : 
            print("** class name missing **")
            return
        
        elif len(args) == 1: 
            HBNBCommand.check_exist_class(args) 
             
        elif len(args) == 2: 
            instance_key = f"{args[0]}.{args[1]}"
            HBNBCommand.check_exist_class(args)
            HBNBCommand.check_exist_id(args, instance_key, all_classes) 
            
        elif len(args) == 3: 
            instance_key = f"{args[0]}.{args[1]}"
            HBNBCommand.check_exist_class(args)
            HBNBCommand.check_exist_id(args, instance_key, all_classes) 

        elif len(args) == 4: 
            instance_key = f"{args[0]}.{args[1]}"
            HBNBCommand.check_exist_class(args)
            if HBNBCommand.check_exist_id(args, instance_key, all_classes) == -1:
                return
            else:
                instance = all_classes[instance_key]
                ins_dict = instance.__dict__

                for key, value in list(ins_dict.items()):
                    if key == args[2]:
                        typ = type(args[2])
                        ins_dict[args[2]] = typ(f"{args[3]}")
                       
                    else:
                        typ = type(args[2])
                        ins_dict[args[2]] = typ(f"{args[3]}")
                       
                storage.save()

                        
if __name__ == '__main__':
    HBNBCommand().cmdloop()