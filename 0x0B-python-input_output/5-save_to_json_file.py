#!/usr/bin/python3
""" define the model json """
from json import dumps


def save_to_json_file(my_obj, filename):
    """ function object to text file """
    with open(filename, mode='w', encoding='utf-8') as fl:
        fl.write(dumps(my_obj))
