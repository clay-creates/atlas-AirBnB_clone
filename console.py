#!/usr/bin/python3
"""
Module containing the console, entry point for command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Place": Place,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, args):
        """Quits the program"""
        return True

    def do_EOF(self, args):
        """Handles EOF and quits program"""
        return True

    def emptyline(self):
        """Does nothing given emptyline"""
        pass

    # def default(self, args):
    #     """Default for undefined commands"""
    #     supported_commands = {
    #         ...
    #     }
    #     if args in supported_commands:
    #         ...
    #     else:
    #         print("Unknown command: {}".format(args))

    def do_create(self, args):
        """
        Creates new instance and saves it to storage. Prints instance id.
        """
        ...

    def do_show(self, args):
        """
        Prints string representation of instance based on class name and id
        """
        ...

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id. Saves to storage.
        """
        ...

    def do_all(self, args):
        """
        Prints the string representation of all instances based or not on the class name
        """
        ...

    def do_update(self, args):
        """
        Updates instance based on class name and id by adding or updating attribute. Saves to storage.
        """
        ...

if __name__ == "__main__":
    HBNBCommand().cmdloop()
