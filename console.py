#!/usr/bin/python3
""" console"""

import cmd
from models.base_model import BaseModel
from models import *


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
        list_args = args.split()
        if (len(list_args) < 2):
            if (list_args[0] not in globals().keys()):
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif (len(list_args) == 2):
            if (list_args[0] not in globals().keys()):
                print("** class doesn't exist **")
                return
            all_objs = storage.all()
            for key, value in all_objs.items():
                class_id = all_objs[key]
                object_id = key.split(".")[1]
                if (the_id == object_id):
                    flag = 0
            if flag:
                print("** no instance found *")
            else:
                print("** attribute name missing **")
        elif (len(list_args) == 3):
            if (list_args[0] not in globals().keys()):
                print("** class doesn't exist **")
                return
            all_objs = storage.all()
            for key, value in all_objs.items():
                class_id = all_objs[key]
                object_id = key.split(".")[1]
                if (the_id == object_id):
                    flag = 0
            if flag:
                print("** no instance found *")
            elif list_args[2].isdigit
            print("** value missing **")

            elif (list_args == 2):
                if (list_args[1] == )

            else:
                flag = 1
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
