#!/usr/bin/env python3
"""
The console for our AirBnB project
"""
import cmd
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """The HBNB command line"""
    all_classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
    cmd.Cmd.prompt = "(hbnb) "

    def emptyline(self, line=""):
        """Makes the command interpreter do nothing on empty line"""
        pass

    def do_quit(self, line):
        """
        A command that will quit the loop of hbnb when the user
        enters quit
        """
        return True

    def do_EOF(self, line):
        """
        A command that will quit the loop of hbnb when the user
        enters quit
        """
        return True

    def help_quit(self):
        """Documentation for quit"""
        print("Quits hbnb loop of hbnb when user enters quit.\n")

    def help_EOF(self):
        """Documentation for EOF"""
        print("Quits hbnb loop when user enters EOF.\n")

    def do_create(self, line):
        """Creates new instances and saves to JSON files and prints id"""
        class_names = line.split(" ")
        if line is None or line == "":
            print("** class name missing **")
        elif class_names[0] not in storage.all_classes:
            print("** class doesn't exists **")
        else:
            new_model = eval("{}()".format(class_names[0]))
            for i in range(1, len(class_names)):
                rex = r'^(\S+)\=(\S+)'
                match = re.search(rex, class_names[i])
                if not match:
                    continue
                key = match.group(1)
                value = match.group(2)
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                    value = value.replace('_', ' ')
                if cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(new_model, key, value)
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """Shows an instance based on id or class name"""
        all_objs = storage.all()
        attrbs = line.split()
        obj_id_avail = 0
        obj_id_avail2 = 0
        obj_name_avail = 0
        if (len(attrbs) > 1):
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                obj_name = type(obj).__name__
                if attrbs[0] == obj_name:
                    obj_name_avail = 1
                    if attrbs[1] == obj.id:
                        obj_id_avail = 1
            if obj_name_avail and obj_id_avail:
                print(obj)
            elif obj_name_avail == 1 and obj_id_avail == 0:
                print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(attrbs) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on id or class name"""
        all_objs = storage.all()
        attrbs = line.split()
        obj_id_avail = 0
        obj_id_avail2 = 0
        obj_name_avail = 0
        if (len(attrbs) > 1):
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                obj_name = type(obj).__name__
                if attrbs[0] == obj_name:
                    obj_name_avail = 1
                    if attrbs[1] == obj.id:
                        obj_id_avail = 1
            if obj_name_avail and obj_id_avail:
                storage.delete(obj)
                storage.save()
            elif obj_name_avail == 1 and obj_id_avail == 0:
                print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(attrbs) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all instances based or not on class name"""
        all_objs = storage.all()
        attrbs = line.split()
        obj_name_avail = 0
        if (len(attrbs) >= 1):
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                obj_name = type(obj).__name__
                if obj_name == attrbs[0]:
                    obj_name_avail = 1
                    print(obj)
            if obj_name_avail == 0:
                print("** class doesn't exist **")
        elif line == "":
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        else:
            pass

    def do_update(self, line):
        """Updates an instance based on class name or id"""
        all_objs = storage.all()
        attrbs = line.split()
        obj_id_avail = 0
        obj_id_avail2 = 0
        obj_name_avail = 0
        if (len(attrbs) > 1):
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                obj_name = type(obj).__name__
                if attrbs[0] == obj_name:
                    obj_name_avail = 1
                    if attrbs[1] == obj.id:
                        obj_id_avail = 1
            if obj_name_avail and obj_id_avail:
                if attrbs[2]:
                    if attrbs[3]:
                        try:
                            obj.__dict__[attrbs[2]] = eval(attrbs[3])
                        except Exception:
                            obj.__dict__[attrbs[2]] = attrbs[3]
                            obj.save()
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
            elif obj_name_avail == 1 and obj_id_avail == 0:
                print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(attrbs) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")

    def count(self, line):
        """Counts the number of all instances"""
        all_objs = storage.all()
        count = 0
        my_list = line.split()
        for obj_id in all_objs.keys():
            if type(all_objs[obj_id]).__name__ == my_list[0]:
                count += 1
        if count == 0:
            print("** class doesn't exist **")
        else:
            print(count)

    def default(self, line):
        """Default command to handle all instances retrieval or their count
        """
        my_list = line.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])
            else:
                cmd.Cmd.default(self, line)

    def help_create(self):
        """Documentation for create""" 
        print("Creates a new instance, saves it to file and print id.\n")

    def help_count(self):
        """Documentation for count"""
        print("Counts the number of instances.\n")

    def help_show(self):
        """Documentation for show"""
        print("Prints a string representation of an instance.\n")

    def help_destroy(self):
        """Documentation for destroy"""
        print("Deletes an instance based on the class name and id\n")

    def help_all(self):
        """Documentation for all"""
        print("Prints all string representation of all instances.\n")

    def help_update(self):
        """Documentation for update"""
        print("Updates an instance by adding or updating an attribute.\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
