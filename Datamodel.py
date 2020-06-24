class Test:

    def __init__(self, one, two):
        self.one = one
        self.two = two

    def __repr__(self):
        return f'{self.one}, {self.two}'

    def __str__(self):
        return f'{self.one, self.two}'


t = Test(1, 2)

print(str(t))