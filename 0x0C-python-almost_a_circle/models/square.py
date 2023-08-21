#!/usr/bin/python3
"""find a square fon model rectangle"""
from models.rectangle import Rectangle
class Square(Rectangle):
    """get teh square"""
     def __init__(self, size: int, x=0, y=0, id=None):
         """get the square"""
         super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self) -> int:
        """get teh square"""
        return self.__size

    @size.setter
    def size(self, value: int):
        """get the square"""
        self.check_type_value('width', value)
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self) -> str:
        """get the square"""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)

    def update(self, *args, **kwargs):
         attr = ['id', 'size', 'x', 'y']
        if args:
            for at, numb in zip(attr, args):
                """get the square"""
                setattr(self, at, numb)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self) -> dict:
        """get the square"""
         id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return {'id': id, 'x': x, 'size': size, 'y': y}
