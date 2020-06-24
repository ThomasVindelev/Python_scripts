import sys

my_list = [i ** 2 for i in range(1000000)]

my_tuple = tuple(i ** 2 for i in range(1000000))

my_gen = (i ** 2 for i in range(1000000))

print(sys.getsizeof(my_list))
# 8697456

print(sys.getsizeof(my_tuple))
# 8000040

print(sys.getsizeof(my_gen))
# 112

