class DunderExample:

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('Called instance')

    def __iter__(self):
        return self
