#!/usr/bin/python3

import cmd
import sys

class HBNBCommand(cmd.Cmd):
	"""A cmd module for building custom shells that let a user work with a program interactively."""
	intro = 'Welcome to the Console.   Type help or ? to list commands.\n'
	prompt = '(hbnb) '

	def do_EOF(self, line):
		"Exit"
		return True

	def do_quit(self, line):
		'"Quit command to exit the program"\n'
		return True

	def emptyline(self):
		pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
