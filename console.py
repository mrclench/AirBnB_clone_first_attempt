#!/usr/bin/python3
"""The console for Airbnb project"""
import cmd
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
