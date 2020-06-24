class Binary:
    def __init__(self, elements):
        self.elements = elements
        self.item = None

        self.right = None
        self.left = None

    def create_node(self, data_entry):
        if self.data:
            if self.data < data_entry:
                if self.right is None:
                    self.right = Binary(data_entry)
                else:
                    self.right.create_node(data_entry)
            elif self.data > data_entry:
                if self.left is None:
                    self.left = Binary(data_entry)
                else:
                    self.left.create_node(data_entry)
        else:
            self.data = data_entry

