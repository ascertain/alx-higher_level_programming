#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
===================================
module with class BaseGeometry
===================================
"""


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Method for initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)#!/usr/bin/python3
"""
more class base
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Square class
"""


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ size init"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return("[Square] " + str(self.__size) + "/" + str(self.__size))
