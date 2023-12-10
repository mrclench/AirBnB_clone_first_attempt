#!/usr/bin/python3
"""The console for Airbnb project"""

import cmd
from models.base_model import BaseModel
from models import storage
import json
import sys

class HBNBCommand(cmd.Cmd):
	"""A cmd module for building custom shells that let a user work with a program interactively."""
	prompt = '(hbnb) '

	def do_EOF(self, line):
		"Exit"
		return True

	def do_quit(self, line):
		'"Quit command to exit the program"\n'
		return True

	def emptyline(self):
		pass

	def do_create(self, line):
		"""Creates a new instance of BaseModel and saves it and prints out its unique id
		Usage: create <class_name>
		"""
		args = line.split()
		if not args:
			print("** class name missing **")
			return

		class_name = args[0]
		if class_name not in storage.classes:
			print("** class doesn't exist **")
			return

		new_instance = storage.classes[class_name]()
		storage.save()
		print(new_instance.id)

	def do_show(self, line):
		"""Prints the string representation of an instance based on the class name and class id"""
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
		key = "{}.{}".format(class_name, instance_id)
		all_objects = storage.all()

		if key not in all_objects:
			print("** no instance found **")
			return

		instance = all_objects[key]
		print(instance)


if __name__ == '__main__':
	HBNBCommand().cmdloop()
