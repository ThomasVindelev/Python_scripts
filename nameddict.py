from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

my_dog = Dog(age=5, breed='Husky', name='Sam')

print(my_dog.name)

print(my_dog[2])

# Sam