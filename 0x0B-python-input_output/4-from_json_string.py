#!/usr/bin/python3
""" define the function json to object """


import json


def from_json_string(my_str):
    """ return object to json """
    return json.loads(my_str)
