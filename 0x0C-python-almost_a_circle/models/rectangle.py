#!/usr/bin/python3
""" define the class rectangle """
from models.base import Base


class Rectangle(Base):
    """ represent the class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize the new class rectangle
        args:
            width : the width of the new Rectangle.
            height : the height of the new Rectangle.
            x : the x coordinate of the new Rectangle.
            y : the y coordinate of the new Rectangle.
            id : the identity of the new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get the width of the rect """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width of the rect """
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get the height of the rect """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height of the rect """
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get the x cordinate of rect """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the x cordinate of rect """
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get the y of the rect """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the y of the rect """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ func to return the area of the rect """
        return self.width * self.height

    def display(self):
        """ func to return the rect using # """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """ funct to update the rectangle
        args:
            *args: new value
                - 1 argument represents id attribute
                - 2 argument represents width attribute
                - 3 argument represent height attribute
                - 4 argument represents x attribute
                - 5 argument represents y attribute
            **kwargs: new key or value pairs or attr
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for a, q in kwargs.items():
                if a == "id":
                    if q is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = q

                elif a == "width":
                    self.width = q
                elif a == "height":
                    self.height = q
                elif a == "x":
                    self.x = q
                elif a == "y":
                    self.y = q

    def to_dictionary(self):
        """ funct to return the dict of rectangle """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
