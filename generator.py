import sys

the = [i for i in range(10000)]

def my_gen(object):
    for i in object:
        yield i

lol = my_gen(the)

print(sys.getsizeof(lol))
print(type(lol))

print(sys.getsizeof(the))

