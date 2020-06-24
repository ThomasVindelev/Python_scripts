class MyManager:

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
        print('Closed file')
        self.file.close()
        self.closed = True


with MyManager('text_file.txt', 'w') as manager:
    print('In with block')
    manager.write('This is the input')

# Opened file
# In with block
# Closed file


