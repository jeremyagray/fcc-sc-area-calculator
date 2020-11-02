import math


class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.height + 2 * self.width

    def get_diagonal(self):
        return math.sqrt(math.pow(self.height, 2) + math.pow(self.width, 2))

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'

        pic = ''
        for i in range(self.height):
            stars = ''
            for j in range(self.width):
                stars += '*'
            pic += stars + '\n'

        return pic

    def get_amount_inside(self, other):
        v = self.height // other.height
        h = self.width // other.width
        return v * h


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return 'Square(side={})'.format(self.side)

    def set_side(self, side):
        self.side = side
        self.height = side
        self.width = side

    def set_height(self, height):
        self.set_side(height)

    def set_width(self, width):
        self.set_side(width)
