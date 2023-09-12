#!/usr/bin/python3
'''exception value class'''

class BaseGeometry:
    '''A BaseGeometry class'''
    def area(self):
        '''exception function'''
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        '''validating the value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
