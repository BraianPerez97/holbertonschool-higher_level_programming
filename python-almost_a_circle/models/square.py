#!/usr/bin/python3
"""Module that contains Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instances"""
        super().__init__(size, x, y, id)

    def __str__(self):
        """str special method"""
        str_square = "[Square]"
        str_id = "({})".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_xy + str_wh

    @property
    def size(self, value):
        """Getter Size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size"""
        self.width = value
        self.height = value

    def __str__(self):
        """String special method"""
        str_rectangle = "[Square]"
        str_id = "({})".format(self.id)
        str_xy = "{}/{} - 
