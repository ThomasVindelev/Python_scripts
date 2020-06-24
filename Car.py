class Car:
    def __init__(self, *args):
        self.make = args[0]
        self.model = args[1]
        self.bhp = args[2]
        self.mph = args[3]

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, make):
        self.__make = make

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def bhp(self):
        return self.__bhp

    @bhp.setter
    def bhp(self, bhp):
        self.__bhp = bhp

    @property
    def mph(self):
        return self.__mph

    @mph.setter
    def mph(self, mph):
        self.__mph = mph


c = Car('BMW', 'i5', '450', '180')


