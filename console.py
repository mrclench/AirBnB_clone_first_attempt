#!/usr/bin/python3
"""The console for Airbnb project"""

import cmd
from models.base_model import BaseModel
from models import storage
import json
import sys

my_instance = BaseModel()

class HBNBCommand(cmd.Cmd):
	"""A cmd module for building custom shells that let a user work with a program interactively."""
	prompt = '(hbnb) '

	def __init__(self, storage=None):
		super().__init__()
		self.storage = storage
		self.classes = ["BaseModel", "User", "Place", "Review", "State", "City", "Amenity"]

	def do_create(self, line):
		"""Creates a new instance of BaseModel and saves it and prints out its unique id
		Usage: create <class_name>
		"""
		args = line.split()
		if not args:
			print("** class name missing **")
			return

		class_name = args[0]
		if class_name not in storage.classes and class_name not in globals():
			print("** class doesn't exist **")
			return

		new_instance = globals()[class_name]()
		storage.save()
		print(new_instance.id)

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

		if class_name not in storage.classes:
			print("** class doesn't exist **")
			return

		if len(args) < 2:
			print("** instance id missing **")
			return

		instance_id = args[1]
		key = "{].{}".format(class_name, instance_id)

		all_objects = storage.all()

		if key not in all_objects:
			print("** no instance found **")
			return

		del all_objects[key]
		storage.save()

	def do_all(self, line):
		"""Prints 'all' string representation of 'all' instances based or not on the class name"""
		args = line.split()
		if not args or args[0] not in self.classes:
			print("** class doesn't exist **")
			return

		class_name = args[0]
		all_objects = storage.all()
		instances = [str(obj) for obj in all_objects.values() if type(obj).__name__ == class_name]
		print(instances)

	def do_update(self, line):
		"""Updates an instance of the class name and id by adding or updating attribute."""
		args = line.split()
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

		attr_value = args[3]
		instance = all_objects[key]

		instance.save()
storage.reload()



if __name__ == '__main__':
	HBNBCommand().cmdloop()
