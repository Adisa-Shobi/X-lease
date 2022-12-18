#!/usr/bin/python3
"""This module contains the type(self) class a
console console class
"""


import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.category import Category
from models.city import City
from models.country import Country
from models.item import Item
from models.review import Review
from models.state import State
from models.user import User


class XLEASE(cmd.Cmd):
    """This is the HBNB web app Console"""
    prompt = "(xlease)"

    cls = {'BaseModel': BaseModel,
           'User': User,
           'Category': Category,
           'Country': Country,
           'City': City,
           'State': State,
           'Item': Item,
           'Review': Review}
    cmd_l = ['create', 'all', 'update', 'show', 'destroy', 'count']
    cls_l = ['BaseModel', 'State', 'Item',
             'Country', 'Category', 'City', 'User', 'Review']

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            arg_l = arg.split('.')
            if len(arg_l) == 2:
                cmd = arg_l[1].split('(')
                args = cmd[1].split(')')
                if arg_l[0] in type(self).cls_l and cmd[0] in type(self).cmd_l:
                    arg = f'{cmd[0]} {arg_l[0]} {args[0]}'
        return arg
    
    def do_create(self, arg):
        """ Create an object of any class"""
        if not arg:
            print("** class name missing **")
            return
        arg = arg.split(' ')
        clss = arg[0]
        dic_t = {}
        if len(arg) > 1:
            args = arg[1:]
            dic_t = {a.split('=')[0]: eval(a.split('=')[1].
                                           replace('_', ' ')) for a in args}
        if clss not in type(self).cls:
            print("** class doesn't exist **")
            return
        if dic_t:
            new_instance = type(self).cls[clss]()
            for k, v in dic_t.items():
                setattr(new_instance, k, v)
        else:
            new_instance = type(self).cls[clss]()
        new_instance.save()
        print(new_instance.id)

    def do_count(self, cls_name):
        """
        Counts the number of instances of a class
        Ex: (xlease) User.count()
            (xlease) count User
        """
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            cls = k.split('.')
            if cls[0] == cls_name:
                count = count + 1
        print(count)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: (xlease) show BaseModel 1234-1234-1234.
            (xlease) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if len(args) > 2:
                return
            if len(args) == 1:
                if args[0] not in type(self).cls.keys():
                    print("** class doesn't exist **")
                    return
                print("** instance id missing **")
                return
            if len(args) == 2:
                arg1 = args[0]
                arg2 = args[1].strip('"')
                obj_id = f'{arg1}.{arg2}'
                if arg1 in type(self).cls.keys():
                    instance = storage.all()
                    if obj_id in instance.keys():
                        print(instance[obj_id])
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: (xlease) destroy BaseModel 1234-1234-1234.
            (xlease) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if len(args) > 2:
                return
            if len(args) == 1:
                if args[0] not in type(self).cls:
                    print("** class doesn't exist **")
                    return
                print("** instance id missing **")
                return
            if len(args) == 2:
                arg1 = args[0]
                arg2 = args[1].strip('"')
                obj_id = f'{arg1}.{arg2}'
                if arg1 in type(self).cls.keys():
                    instance = storage.all()
                    if obj_id in storage.all(): # instance.keys():
                        n_i = storage.all().pop(obj_id)
                        storage.delete(n_i)
                        # del instance[obj_id]
                        # # storage.delete(instance[obj_id])
                        # new_instance = type(self).cls[arg1](**instance)
                        # # new_instance.delete()
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: (xlease) all BaseModel
            (xlease) User.all()
            (xlease) all
        """
        inst_list = []
        if not line:
            instance = storage.all()
            for key in instance.keys():
                inst_list.append(str(instance[key]))
            print(inst_list)
            return
        else:
            args = line.split()
            if len(args) > 1:
                return
            if len(args) == 1:
                if args[0] in type(self).cls.keys():
                    instance = storage.all()
                    for key in instance.keys():
                        if key.split('.')[0] == args[0]:
                            inst_list.append(str(instance[key]))
                    print(inst_list)
                    return
                else:
                    print("** class doesn't exist **")
                    return

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file).
        Ex: (xlease) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
            (xlease)  User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
        """
        dict_flag = 0
        if not line:
            print("** class name missing **")
        else:
            if '{' in line:
                line_l = line.split(' {')[1]
                dict_flag = 1
            args = line.split()
            obj = {}
            c_flag = 0
            id_flag = 0
            attr_flag = 0
            if len(args) >= 1:
                if args[0] not in type(self).cls.keys():
                    print("** class doesn't exist **")
                    return
                else:
                    if len(args) > 1:
                        c_flag = 1
                    else:
                        print("** instance id missing **")
                        return
            if len(args) >= 2:
                if c_flag == 0:
                    return
                else:
                    arg1 = args[1].strip(',').strip('"')
                    obj_id = f"{args[0]}.{arg1}"
                    instance = storage.all()
                    if args[0] in type(self).cls.keys():
                        if obj_id in instance.keys():
                            if len(args) > 2:
                                id_flag = 1
                            else:
                                print("** attribute name missing **")
                                return
                        else:
                            print("** no instance found **")
                            return
            if len(args) >= 3:
                if dict_flag == 1:
                    arg_str = "{" + line_l
                    arg_str = arg_str.replace('\'', '"')
                    try:
                        arg_dict = json.loads(arg_str)
                    except Exception:
                        print("** attribute name missing **")
                        return
                    if isinstance(arg_dict, dict):
                        obj = instance[obj_id]
                        try:
                            for k, v in arg_dict.items():
                                setattr(obj,
                                        k.strip('"'),
                                        v.strip('"')
                                        if isinstance(v, str) else v)
                            obj.save()
                            return
                        except Exception:
                            print("** attribute name missing **")
                            return
                if id_flag == 0:
                    return
                else:
                    obj = instance[obj_id]
                    if len(args) > 3:
                        setattr(obj, args[2].strip(',').strip('"'),
                                args[3].strip(',').strip('"'))
                        obj.save()
                    else:
                        print("** value missing **")
                        return

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        return True

    def emptyline(self):
        """Do nothing when line is empty"""
        pass

    def help_help(self):
        """ Prints command (help) description """
        print("Provides description of selected command")


if __name__ == '__main__':
     XLEASE().cmdloop()
