import sys

my_list = [i ** 2 for i in range(100000)]

my_gen = (i ** 2 for i in range(100000))

print(sys.getsizeof(my_list))
# 824456

print(sys.getsizeof(my_gen))
# 112

