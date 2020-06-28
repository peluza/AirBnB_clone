#!/usr/bin/python3
""" console"""

import cmd
from models.base_model import BaseModel
from models import *
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
        if (len(the_class) == 0):
            print("** class name missing **")
        else:
            if (the_class not in globals().keys()):
                print("** class doesn't exist **")
            else:
                new_instance = globals()[the_class]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, args):
        if not args:
            print("** class name missing **")
            return
        try:
            the_class, the_id = args.split(" ")
            if (the_class not in globals().keys()):
                print("** class doesn't exist **")
            else:
                flag = 1
                all_objs = storage.all()
                for key, value in all_objs.items():
                    class_id = all_objs[key]
                    object_id = key.split(".")[1]
                    if (the_id == object_id):
                        print(value)
                        flag = 0
                if flag:
                    print("** no instance found *")
        except:
            if (args not in globals().keys()):
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

    def do_destroy(self, args):
        if not args:
            print("** class name missing **")
            return
        try:
            the_class, the_id = args.split(" ")
            if (the_class not in globals().keys()):
                print("** class doesn't exist **")
            else:
                flag = 1
                all_objs = storage.all()
                for key, value in all_objs.items():
                    class_id = all_objs[key]
                    object_id = key.split(".")[1]
                    if (the_id == object_id):
                        del all_objs[key]
                        storage.save()
                        flag = 0
                        break
                if flag:
                    print("** no instance found *")
        except:
            if (args not in globals().keys()):
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

    def do_update(self, args):
        if not args:
            print("** class name missing **")
            return
        list_args = shlex.split(args, posix=False)
        print(list_args)
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
        # print(list_args[2].__repr__())
        print(list_args[2][0])
        print(list_args[2])
        name = list_args[2].split()
        name = list_args[2].strip('\"')
        if list_args[3][0] == "'":
            value = list_args[3].split()
        value = list_args[3].strip('\"')
        old_dic.__dict__[name] = value
        storage.save()

    def do_all(self, the_class):
        if (len(the_class) == 0):
            the_class = "BaseModel"
        if (the_class not in globals().keys()):
            print("** class doesn't exist **")
            return
        else:
            lista = []
            all_objs = storage.all()
            for key, value in all_objs.items():
                lista.append(value.__str__())
            print(lista)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
