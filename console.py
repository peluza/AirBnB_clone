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
                line = globals()[the_class]()
                line.save()
                print(line.id)

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
                print("** class doesn't exist --> **")
            else:
                flag = 1
                new_objet = {}
                all_objs = storage.all()
                for key, value in all_objs.items():
                    class_id = all_objs[key]
                    object_id = key.split(".")[1]
                    if (the_id != object_id):
                        new_objet[key] = value
                        flag = 0
                storage.__objects = new_objet
                # storage.save()
                print("des ---",new_objet)
                print("des --->", storage.__objects)
                if flag:
                    print("** no instance found *")
        except:
            if (args not in globals().keys()):
                print("** --> class doesn't exist **")
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
