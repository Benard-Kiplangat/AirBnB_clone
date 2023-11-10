#!/usr/bin/env python3
"""
The console for our AirBnB project
"""
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
