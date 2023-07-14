#!/usr/bin/python3
""" define json file """
import json


def load_from_json_file(filename):
    """ function to load from json file """
    with open(filename) as fl:
        return json.load(fl)
