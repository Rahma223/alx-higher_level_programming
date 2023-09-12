#!/usr/bin/python3
'''subclass'''

Rectangle = __import__('9-rectangle.py').Rectangle

class Square(Rectangle):
    '''A subclass square'''
    def __init__(self, size):
        '''constractor'''
        self.integer_validator = ("size", size)
        self.size = size
        super().__init__(size, size)

    def area(self):
        '''return area of square'''
        return self.__size ** 2

    def __str__(self):
        '''String function'''
        return "[Square]" + str(self.__size) "/" + str(self.__size)
