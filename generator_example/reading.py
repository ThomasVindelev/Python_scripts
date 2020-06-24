import sys


class NewReader:

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        print('Opened file')
        self.closed = False
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print('Closed file')
        self.closed = True


def reader_decorator(func):
    def wrapper(*args):
        letters = func(*args)
        for i in letters:
            print(i)
        print(sys.getsizeof(letters))
        return letters
    return wrapper


