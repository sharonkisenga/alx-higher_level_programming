#!/usr/bin/python3
"""get it me a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """do the rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """do the rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """do the rectangle class"""
        return self.__width

    @width.setter
    def width(self, value):
        """do the retcangle class"""
        self.int_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """do the rectangle class"""
        return self.__height

    @height.setter
    def height(self, value):
        """do the rectangle class """
        self.int_validation("height", value)
         self.__height = value

    @property
    def x(self):
        """find the rectangle class"""
        return self.__x

    @x.setter
    def x(self, value):
        """do the rectangle x"""
        self.int_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """do the class rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """do the class rectangle"""
        self.int_validation("y", value)
        self.__y = value

    def int_validation(self, name, value):
        """do initialize the validation"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (name == "height" or name == "width") and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if (name == "y" or name == "x") and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))
          def area(self):
        """make an area"""
        return self.__height * self.__width

    def display(self):
        """do the display of a rectangle"""
        rect = "" + ' ' * self.__x
        rect += str('#') * self.__width
        rect = '\n' * self.__y + '\n'.join(
                    list(rect for index in range(self.__height)))
        print(rect)

    def __str__(self):
        """do a class rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """do a class rectangle"""
        index = 0
        if args is not None and len(args) != 0:
            for argument in args:
                index += 1
                if index == 1:
                    self.id = argument
                elif index == 2:
                    self.__width = argument
                elif index == 3:
                    self.__height = argument
                elif index == 4:
                    self.__x = argument
                elif index == 5:
                    self.__y = argument
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        """do a class rectangle"""
        dictionary = {}
        for index in ["id", "width", "height", "x", "y"]:
            dictionary[index] = getattr(self, index)
        return dictionary
