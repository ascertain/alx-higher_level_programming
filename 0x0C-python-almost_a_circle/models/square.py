#!/usr/bin/python3
""" define the class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ represent the class square """

    def __init__(self, size, x=0, y=0, id=None):
        """ initiallize the class square """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get the size of square """
        return self.width

    @size.setter
    def size(self, value):
        """ set the size of the square """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ func to set the square """

        if args and len(args) != 0:
            s = 0

            for arg in args:
                if s == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)

                    else:
                        self.id = arg
                elif s == 1:
                    self.size = arg
                elif s == 2:
                    self.x = arg
                elif s == 3:
                    self.y = arg
                s += 1

        elif kwargs and len(kwargs) != 0:
            for z, q in kwargs.items():

                if z == "id":
                    if q is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = q

                elif z == "size":
                    self.size = q
                elif z == "x":
                    self.x = q
                elif z == "y":
                    self.y = q

    def to_dictionary(self):
        """ return the dic """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        """ return the data and print it """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
