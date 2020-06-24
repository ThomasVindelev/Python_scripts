class Instrument:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


class Guitar(Instrument):

    def __init__(self, brand, strings, price):
        super().__init__(price=price)
        self.__brand = brand
        self.__strings = strings

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def strings(self):
        return self.__strings

    @strings.setter
    def strings(self, strings):
        self.__strings = strings


g = Guitar(brand='Fender', price=100, strings=6)

print(g.price)
# 100
print(g.brand)
# Fender
print(g.strings)
# 6

