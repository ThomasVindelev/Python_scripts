import timeit


s = """
names = ['Thomas', 'Nick', 'Marco', 'Markus', 'Joachim']

for i in range(len(names)):
    print(names[i])
    
    numbers = [i for i in range(10000)]
... for number in numbers:
...     print(number)
"""



timeit.timeit(stmt=s, number=10000)

# 0.1.87493489000002

# 3.569397095999989









upper = ['HELLO', 'WORLD', 'TODAY', 'IS', 'A', 'GREAT', 'DAY']


# 1.3132394689998819

# 1.1507777400001942