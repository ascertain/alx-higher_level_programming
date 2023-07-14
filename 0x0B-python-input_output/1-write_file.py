#!/usr/bin/python3
""" define a test file """


def write_file(filename="", text=""):
    """ write the string to utf8 """

    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
