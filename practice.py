class my_class:

    def __init__(self, number):
        self.number = number
        self.collect = []

    def __add__(self, other):
        self.number += other

    def __call__(self, *args, **kwargs):
        print(self.collect)

    def __repr__(self):
        return str(self.collect)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.number:
            self.n += 1
            return self.n-1
        else:
            raise StopIteration


def my_dec(func):
    def wrapper(*args, **kwargs):
        print('Doing some stuff before')
        func(*args, **kwargs)
        print('Doing some stuff after')
    return wrapper


@my_dec
def to_be_decorated(*args, **kwargs):
    for arg in args:
        print(f'This arg {arg} is passed through this function')
    for key, value in kwargs.items():
        print(f'{key}, {value} was passed through this function')
    print("I'm done now")
