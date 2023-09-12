#!/usr/bin/python3
'''is instance directly or indirectly class'''

def inherits_from(obj, a_class):
    '''instance directly or indirectly class'''
    return isinstance(obj, a_class) and type(obj) != a_class
