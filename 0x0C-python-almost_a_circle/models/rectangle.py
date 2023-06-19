#!/usr/bin/python3
"""This is a rectangle module"""


from models.base import Base
class Rectangle(Base):
    """This is the Rectangle class that inherits from a the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format("width"))
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format("height"))
        if not isinstance(x, int):
            raise TypeError("{} must be an integer".format("x"))
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format("y"))
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))
        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format("width"))
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format("height"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = height

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("{} must be an integer".format("x"))
        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format("y"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -"
                f" {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.__width = args[i]
            if i == 2:
                self.__height = args[i]
            if i == 3:
                self.__x = args[i]
            if i == 4:
                self.__y = args[i]
        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            if k == "width":
                self.__width = v
            if k == "height":
                self.__height = v
            if k == "x":
                self.__x = v
            if k == "y":
                self.__y = v

    def to_dictionary(self):
        return {
            "id" : self.id,
            "width" : self.__width,
            "height" : self.__height,
            "x" : self.__x,
            "y" : self.__y
        }
