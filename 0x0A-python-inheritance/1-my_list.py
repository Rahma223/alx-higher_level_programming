#!/usr/bin/python3
'''myList class'''

class MyList(list):
    """Implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """print sorted integer numbers"""
        print(sorted(self))
