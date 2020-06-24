class Color:

    """ Handles RGB colors form 0 to 255
        >>> print(Color(255, 0, 0) + Color(255, 0, 0))
        Color(r:255, g:0, b:0)
        >>> print(Color(255, 0, 0) - Color(255, 0, 0) - Color(255, 0, 0))
        Color(r:0, g:0, b:0)
        >>> print(Color(255, 0, 0) - Color(255, 0, 0) + Color(0, 10, 0) - Color(255, 0, 0))
        Color(r:0, g:10, b:0)
    """

    def __init__(self, r, g, b):
        self.r = max(min(255, r), 0)
        self.g = max(min(255, g), 0)
        self.b = max(min(255, b), 0)

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __sub__(self, other):
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)

    def __str__(self):
        return f"Color(r:{self.r}, g:{self.g}, b:{self.b})"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
