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
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        elif value <= 0:
            raise ValueError("Width must be an integer")
        self.width = value
        self.height = value

    def __str__(self):
        """String special method"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
