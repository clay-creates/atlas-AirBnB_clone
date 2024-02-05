#!/usr/bin/python3
"""
Module containing the console, entry point for command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = ' (hbnb) '

    def do_quit(self, args):
        """Quits the program"""
        return True

    def do_EOF(self, args):
        """Handles EOF and quits program"""
        return True

    def emptyline(self):
        """Does nothing given emptyline"""
        pass

    def default(self, line):
        """Default for undefined commands"""
        print("Unknown command: {}".format(line))

    def do_help(self, args):
        """List available commands with 'help' or '?'"""
        print("Available commands:")
        for command in sorted(self.get_names()):
            print("  ", command)

if __name__ == "__main__":
    HBNBCommand().cmdloop
