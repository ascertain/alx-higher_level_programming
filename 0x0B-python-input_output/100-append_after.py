#!/usr/bin/python3
""" deifn the function append """


def append_after(filename="", search_string="", new_string=""):
    """ insert text after each line """

    txt = ""

    with open(filename) as rx:
        for li in rx:
            txt += li

            if search_string in li:
                txt += new_string

    with open(filename, "w") as wr:
        wr.write(txt)
