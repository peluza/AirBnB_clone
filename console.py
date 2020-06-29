#!/usr/bin/python3
""" console"""

import cmd
from models import *
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ' '

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        """ Quit command to exit the program """
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_create(self, the_class):
        if not the_class:
            print("** class name missing **")
            return

        if (the_class not in globals().keys()):
            print("** class doesn't exist **")
        else:
            new_instance = globals()[the_class]()
            new_instance.save()
            print(new_instance.id)
            return

    def do_show(self, args):
        if not args:
            print("** class name missing **")
            return
        list_args = args.split(" ")
        if (list_args[0] not in globals().keys()):
            print("** class doesn't exist **")
            return
        if (len(list_args) <= 1):
            print("** instance id missing **")
            return
        all_objs = storage.all()
        classN_id = list_args[0] + "." + list_args[1]
        if classN_id not in all_objs:
            print("** no instance found *")
            return
        print(all_objs[classN_id])
        return

    def do_destroy(self, args):
        if not args:
            print("** class name missing **")
            return
        list_args = args.split(" ")
        if (list_args[0] not in globals().keys()):
            print("** class doesn't exist **")
            return
        if (len(list_args) <= 1):
            print("** instance id missing **")
            return
        all_objs = storage.all()
        classN_id = list_args[0] + "." + list_args[1]
        if classN_id not in all_objs:
            print("** no instance found *")
            return
        del all_objs[classN_id]
        storage.save()
        return

    def do_update(self, args):
        if not args:
            print("** class name missing **")
            return
        args = args.replace("'", "")
        list_args = shlex.split(args, posix=False)
        if list_args[0] not in globals().keys():
            print("** class doesn't exist **")
            return
        if len(list_args) <= 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        className_id = list_args[0] + "." + list_args[1]
        if className_id not in all_objs:
            print("** no instance found *")
            return
        if len(list_args) <= 2:
            print("** attribute name missing **")
            return
        if len(list_args) <= 3:
            print("** value missing **")
            return
        old_dic = all_objs[className_id]
        name = list_args[2].strip('\"')
        value = list_args[3].strip('\"')
        setattr(old_dic, name, value)
        # old_dic.__dict__[name] = value
        BaseModel.save(self)
        return

    def do_all(self, the_class):
        if (the_class and the_class not in globals().keys()):
            print("** class doesn't exist **")
            return
        lista = []
        all_objs = storage.all()
        print(all)
        for key, value in all_objs.items():
            lista.append(value.__str__())
        print(lista)
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
