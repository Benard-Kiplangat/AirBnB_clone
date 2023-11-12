#!/usr/bin/env python3
"""
The console for our AirBnB project
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    cmd.Cmd.prompt = "(hbnb)"

    def emptyline(self, line):
        """
        A command to make the hbnb command interpreter do nothing
        on an empty line
        """
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
        print("\nQuits hbnb loop of hbnb when user enters quit")

    def help_EOF(self):
        print("\nQuits hbnb loop when user enters EOF")

    def do_create(self, line):
        """Creates new instances and saves to JSON files and prints id"""
        if line == "":
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exists **")
        else:
                new_model = BaseModel()
                new_model.name = line
                new_model.my_number = 89
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
                if attrbs[0] == obj.name:
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
                if attrbs[0] == obj.name:
                    obj_name_avail = 1
                    if attrbs[1] == obj.id:
                        obj_id_avail = 1
            if obj_name_avail and obj_id_avail:
                del obj
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
        for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                if line:
                    if obj.name == line:
                        print(obj)
                else:
                    print(obj)

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
                if attrbs[0] == obj.name:
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

    def help_create(self):
        print("\nCreates a new instance of BaseModel, saves it to JSON \
                file and prints the id.")

    def help_show(self):
        print("\nPrints a string representation of an instance based \
                on class name and id.")

    def help_destroy(self):
        print("\nDeletes an instance based on the class name and id")

    def help_all(self):
        print("\nPrints all string representation of all instances based\
                or not on the class name.")

    def help_update(self):
        print("\n Updates an instance based on the class name and id by \
                by adding or updating attribute.")


if __name__ == "__main__":
    HBNBCommand().cmdloop()