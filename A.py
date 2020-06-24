class A:
    def __init__(self):
        self.a = 42

    def message(self, msg):
        self.msg = msg


a = A()

print(a.a)


class B:
    def __init__(self):
        self.b = 47


class C(A, B):
    def __init__(self):
        super().__init__()
        print(self.a)


class Color:

    """ Handles RGB colors form 0 to 255 """

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


red = Color(255, 0, 0)
green = Color(0, 255, 0)
blue = Color(0, 0, 255)
purple = Color(255, 0, 255)

print(red)
print(red + blue)
print(purple - red)
print(red + red + red + red)


class Dashboard:
    pass


class Car:
    def __init__(self):
        self.dashboard: Dashboard()


