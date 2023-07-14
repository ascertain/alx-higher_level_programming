#!/usr/bin/python3
""" define the function a file append """


def append_write(filename="", text=""):
    """ function to append the string """

    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
