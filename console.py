#!/usr/bin/env python3
"""Module for the console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone."""
    # Command prompt
    prompt = "(hbnb)" 

    def do_create(self, arg):
        """Create a new instance of a model, save it to storage, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = globals()[arg]()  # Dynamically create instance from class name
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Show all instances of a specific class, or all instances if no class is specified."""
        if arg:
            if arg not in globals():
                print("** class doesn't exist **")
                return
            objs = [str(obj) for obj in storage.all().values() if type(obj).__name__ == arg]
        else:
            objs = [str(obj) for obj in storage.all().values()]
        print(objs)

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter."""
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
