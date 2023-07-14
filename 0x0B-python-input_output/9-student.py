#!/usr/bin/python3
""" define the class student """


class Student:
    """ represent the class student """

    def __init__(self, first_name, last_name, age):
        """ initialize the function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return the get dic """
        return self.__dict__
