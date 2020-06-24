from generator_example.reading import reader_decorator as decorator
from generator_example.reading import NewReader as Reader


@decorator
def read_from_file():
    with Reader('file.txt', 'r') as file:
        for line in file.readline():
            yield line


read_from_file()

# 520


