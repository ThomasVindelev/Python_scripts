class Account:

    def __init__(self, number, pin):
        self.number = number
        self.__pin = pin

    def print_pin(self):
        print(self.__pin)


a = Account('100', '1234')

print(a.pin)

# AttributeError: 'account'
# object has no attribute 'pin'

a.print_pin()
print(a._Account__pin)

# 1234

