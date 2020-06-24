class MyIterable:

    def __init__(self, maximum=0):
        self.maximum = maximum

    def __iter__(self):
        self.iterable = 0
        return self

    # lifts 2 to the power of iterable
    def __next__(self):
        if self.iterable <= self.maximum:
            result = 2 ** self.iterable
            self.iterable += 1
            return result
        else:
            raise StopIteration


a = MyIterable(10)

for n in a:
    print(n)

# 1
# 2
# ...
# 1024


