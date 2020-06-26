#!/usr/bin/python3
""" console"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        """ Quit command to exit the program """
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def create(self, line):
        line = BaseModel()
        print(line.id)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
