#!/usr/bin/python3
"""The console for Airbnb project"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

my_instance = BaseModel()
storage = FileStorage()
storage.reload()


class HBNBCommand(cmd.Cmd):
    """A cmd module for building custom shells that let a user work with a program interactively."""
    __classes_allowed = ["BaseModel", "User", "Place", "Review", "State", "City", "Amenity"]
    prompt = '(hbnb) '

    def __init__(self):
        super().__init__()
        self.storage = storage
        self.classes = ["BaseModel", "User", "Place", "Review", "State", "City", "Amenity"]
        storage.reload()

    def first_class_name_checks(self, command_args):
        """Perform first checks on the command arguments"""
        if not command_args:
            print("** class name missing **")
            return False
        return True

    def do_create(self, command_args):
        """create the object in console"""
        if not self.first_class_name_checks(command_args):
            return

        class_name = command_args.split()[0]

        if class_name not in HBNBCommand.__classes_allowed:
            print("** class doesn't exist **")
            return

        object_to_create = globals()[class_name]()
        storage.new(object_to_create)
        storage.save()
        print(object_to_create.id)

    def do_EOF(self, line):
        "Exit"
        return True

    def do_quit(self, line):
        '"Quit command to exit the program"\n'
        return True

    def emptyline(self):
        pass

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and class id"""
        args = line.split()
        if not args or args[0] not in self.classes:
            print("** class name missing **")
            return

        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")
            return

        instance = all_objects[key]
        print(instance)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (saves update to the JSON file)."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in HBNBCommand.__classes_allowed:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")
            return

        del all_objects[key]
        storage.save()

    def do_all(self, command_args):
        """Prints string representation of all instances in the console"""
        class_name = command_args.split()[0] if command_args else None
        stored_objects = storage.all()

        if class_name and class_name not in self.__classes_allowed:
            print("** class doesn't exist **")
            return

        filtered_objects = [str(obj) for key, obj in stored_objects.items() if
                            not class_name or key.split('.')[0] == class_name]
        print(filtered_objects)

    def do_update(self, command_args):
        """Updates an instance of the class name and id by adding or updating attribute."""
        args = command_args.split()
        if not args or args[0] not in self.classes:
            print("** class name missing **" if not args else "** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        all_objects = storage.all()

        key = "{}.{}".format(class_name, instance_id)
        if key not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3].strip('"')
        instance = all_objects[key]

        # Update the attribute in the instance
        setattr(instance, attr_name, attr_value)
        instance.save()


storage = FileStorage()
storage.reload()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
