def new_decorator(original_func):
    def wrapper():
        print('Some other code before execution')
        original_func()
        print('Some other code after execution')

    return wrapper


@new_decorator
def to_be_decorated():
    print([x for x in range(0, 10, 2)])


to_be_decorated()

