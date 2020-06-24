import sys

def single_addition(n1, n2):
    return n1 + n2


def double_addition(n1, n2, n3):
    return n1 + n2 + n3


def addition(*numbers):
    x = 0
    for n in numbers:
        x += n
    return x

"""

comprehension = [n for n in numbers if n % 2 == 0 if n % 3 == 0 if n not in banned]
"""

numbers = [i for i in range(0, 101)]

banned = [6, 30, 60, 84]


def classic(nums):
    my_list = []
    for n in nums:
        if n % 2 == 0 and n % 3 == 0 and n not in banned:
            my_list.append(n)
    return my_list


new_list = classic(numbers)

print(addition(1, 2, 3, 4))

# 10


def add_to_inventory(**new_order):
    for item, amount in new_order.items():
        print(f'We have received {amount} {item}')


add_to_inventory(apples=10, bananas=20, lemons=30)

# We have received 10 apples
# We have received 20 bananas
# We have received 30 lemons

names = ['Thomas', 'Nick', 'Marco', 'Markus', 'Joachim']

for i in range(len(names)):
    print(i)
    print(names[i])

for name in names:
    print(name)

for i in range(len(names)-1, -1, -1):
    print(names[i])

for name in reversed(names):
    print(name)