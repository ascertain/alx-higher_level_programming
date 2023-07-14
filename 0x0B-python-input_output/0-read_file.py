#!/usr/bin/python3
""" define the function text file """


def read_file(filename=""):
    """ print the content """
    with open(filename, 'r', encoding='UTF-8') as fl:
        print(fl.read(), end="")
