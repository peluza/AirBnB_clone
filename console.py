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
import re


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ' '

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def find_class(self, the_class):
        """ Return True if the class is found in the list """
        list_class = ["BaseModel", "User", "City",
                      "Place", "Amenity", "Review", "State"]
        if the_class in list_class:
            return True
        return False

    def do_create(self, the_class):
        """Creates a new instance of the specific class
saves the object (to the JSON file) and prints the id
[Usage: create <class name> <id>]"""
        if not the_class:
            print("** class name missing **")
            return
        check_class = self.find_class(the_class)
        if (check_class is False):
            print("** class doesn't exist **")
        else:
            new_instance = globals()[the_class]()
            new_instance.save()
            print(new_instance.id)
            return

    def do_show(self, args):
        """Print the string representation of the obj
[Usage: show <class name> <id>]"""
        if not args:
            print("** class name missing **")
            return
        list_args = args.split(" ")
        check_class = self.find_class(list_args[0])
        if (check_class is False):
            print("** class doesn't exist **")
            return
        if (len(list_args) <= 1):
            print("** instance id missing **")
            return
        all_objs = storage.all()
        classN_id = list_args[0] + "." + list_args[1]
        if classN_id not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[classN_id])
        return

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
[Usage: destroy <class name> <id>]"""
        if not args:
            print("** class name missing **")
            return
        list_args = args.split(" ")
        check_class = self.find_class(list_args[0])
        if (check_class is False):
            print("** class doesn't exist **")
            return
        if (len(list_args) <= 1):
            print("** instance id missing **")
            return
        all_objs = storage.all()
        classN_id = list_args[0] + "." + list_args[1]
        if classN_id not in all_objs:
            print("** no instance found **")
            return
        del all_objs[classN_id]
        storage.save()
        return

    def do_update(self, args):
        """ Updates an instance based on the class and id
[Usage: <class name> <id>]
        """
        if not args:
            print("** class name missing **")
            return
        args = args.replace("'", "")
        list_args = shlex.split(args, posix=False)
        check_class = self.find_class(list_args[0])
        if (check_class is False):
            print("** class doesn't exist **")
            return
        if len(list_args) <= 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        className_id = list_args[0] + "." + list_args[1]
        if className_id not in all_objs:
            print("** no instance found **")
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
        BaseModel.save(old_dic)
        return

    def do_all(self, the_class):
        if the_class is "":
            lista = []
            all_objs = storage.all()
            for key, value in all_objs.items():
                lista.append(value.__str__())
            print(lista)
            return
        check_class = self.find_class(the_class)
        if check_class is False:
            print("** class doesn't exist **")
        else:
            lista = []
            all_objs = storage.all()
            for key, value in all_objs.items():
                if key.split(".")[0] == the_class:
                    lista.append(value.__str__())
            print(lista)
        return

    def count_class(self, the_class):
        count = 0
        all_objs = storage.all()
        for key, value in all_objs.items():
            if key.split(".")[0] == the_class:
                count += 1
        return count

    def default(self, args):
        do_braces_split = False
        list_args = args.split(".")
        check_class = self.find_class(list_args[0])
        if len(list_args) > 1 and check_class:
            if list_args[1] == "all()":
                return self.do_all(list_args[0])
            elif list_args[1] == "count()":
                count = self.count_class(list_args[0])
                print(count)
                return
            function = list_args[1].replace(
                "(", " ").replace(")", " ").replace(",", "")
            func_args = shlex.split(function)
            # concatenamos Class_name, espacio, id
            classN_id = list_args[0] + " " + func_args[1]
            if func_args[0] == "show":
                return self.do_show(classN_id)
            elif func_args[0] == "destroy":
                return self.do_destroy(classN_id)

            if func_args[0] == "update":
                if "{" in list_args[1] and "}" in list_args[1]:
                    do_braces_split = True
                if do_braces_split == False:
                    classN_id_args = classN_id + " " + \
                        "\"" + func_args[2] + "\"" + " " + \
                        "\"" + func_args[3] + "\""
                    print("updatted")
                    return self.do_update(classN_id_args)

                elif do_braces_split:
                    func = list_args[1].split("(")[0]
                    id_args = re.compile(
                        "\(([^)]*)\)").split(list_args[1])[1]
                    dic_args = re.compile("\{([^}]*)\}").split(id_args)[1]
                    dic_ = "{" + dic_args + "}"
                    try:
                        s = eval(dic_)
                        if (type(s) is dict):
                            dic_ = dic_args.replace(":", "").replace(",", "")
                            dic_args = shlex.split(dic_)
                            print(dic_args)
                            quo = "\""
                            es = " "
                            j = 0
                            for i in range(int(len(dic_args) / 2)):
                                inp = classN_id + " " + quo + \
                                    dic_args[j] + quo + " " + \
                                    quo + dic_args[j+1] + quo
                                j = j + 2
                                self.do_update(inp)
                                print("updated")
                                return
                    except:
                        pass
            print("*** Unknown syntax: {}".format(args))
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
