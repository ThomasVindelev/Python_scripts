import module_example_context as context

def inventory_tracker(func):
    def wrapper(*args):
        new_list = func(*args)
        with context.MyContext('book.txt', 'w'):
            print('Started writing')
            for l in new_list:
