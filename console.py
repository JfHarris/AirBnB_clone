#!/usr/bin/python3
"""
This is the console that the user inputs commands into
"""


import cmd

from engine import file_storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Console class basic init"""
    intro = "Welcome to AirBnB!"
    prompt = "(hbnb)"
    file = None
    
    __class_list = {
        BaseModel.__name__: BaseModel,
        User.__name__: User,
        State.__name__: State,
        City.__name__: City,
        Place.__name__: Place,
        Amenity.__name__: Amenity,
        Review.__name__: Review
    }
    __class_funcs = ["all", "count", "show", "destroy", "update"]


    @staticmethod
    def parse(arg):
        """Convert args into tuples for interpretation"""
        arg_list = arg.split(id)
        narg_list = []

        for a in arg_list:
            if a != '':
                narg_list.append(a)
        return narg_list

    @classmethod
    def create(self):

    @classmethod
    def show(self, cls):
        pass

    @classmethod
    def destroy(self):

    @classmethod
    def default(self):

    @classmethod
    def all(self):

    @classmethod
    def update(self, cls):
        pass

    @classmethod
    def empty_line(self):
        """
        Does nothing. It's an empty line
        Overrides emptyline function
        """
        pass

    @classmethod
    def save(self, arg):
        """Save function"""
        self.file = open(arg, 'w')
    
    @classmethod
    def count(self, arg):
        """
        print number of elements in filestorage
        that are instances of cls
        """
        arg_list = HBNBCommand.parse(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__class_list:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(arg_list) == 0:
                    obj1.append(obj.__str__())

    @staticmethod
    def parse(arg, id=''):
        """Parser for the console"""


    @classmethod
    def do_quit(self):
        """Quits the program"""
        return True

    @classmethod
    def help_quit(self):
        """Prints help message about quit command"""
        print("Quit command to exit the program\n")

    @classmethod
    def do_EOF(self):
        """End of file"""
        print("")
        return True


    @classmethod
    def close(self):
        """Close the Console"""
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()