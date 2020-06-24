my_list = [10, 7, 8, 5, 9, 11, 4]


class Tree:

    def __init__(self, elements):
        self.elements = elements
        self.data = None
        self.left = None
        self.right = None

    def initialize(self, new_list):
        for e in new_list:
            self.add(e)

    def add(self, new_element):
        if new_element is list:
            self.initialize(new_element)
        if new_element is not list:
            if self.data:
                if self.data > new_element:
                    if self.left is None:
                        self.left = Tree(new_element)
                    else:
                        self.left.add(new_element)
                elif self.data < new_element:
                    if self.right is None:
                        self.right = Tree(new_element)
                    else:
                        self.left.add(new_element)
            else:
                self.data = new_element

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

   # def delete(self, number_to_delete):
   #     temp_list = []
   #     if self.left:
   #         if self.left is not number_to_delete:
   #             temp_list.append(self.left)
   #         else:
   #
   #     print(self.data)
   #     if self.right:
   #         self.right.print_tree()

class Initializer:
    def __init__(self, elements):
        self.elements = elements
        self.new_tree = Tree(None)

    def create_tree(self, elements):
        self.new_tree.add(elements)
        self.new_tree.print_tree()


A = Initializer(my_list)

A.create_tree(my_list)



