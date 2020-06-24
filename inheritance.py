my_list = []

for i in range(1, 11):
    if i % 2 == 0:
        my_list.append(i)


my_list = [i for i in range(1, 11) if i % 2 == 0]


my_file = open('file.txt', 'w')

try:
    my_file.write('This is written to the file')
finally:
    my_file.close()


with open('file.txt', 'w') as my_file:
    my_file.write('This is written to the file')


fruits = ['apple', 'banana', 'lemon']

for i in range(len(fruits)):
    print(i+1, fruits[i])


for i, fruit in enumerate(fruits, 1):
    print(i, fruit)

