class Square:

    type = "polygon"

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Rectangle(Square):

    def __init__(self, length, width):
        super().__init__(length, width)

