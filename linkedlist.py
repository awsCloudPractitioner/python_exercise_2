from node import Node


class SingleLinkedList:

    #  start_node will be empty at the time of linked list creation
    def __init__(self):
        self.start_node = None

    # enter the number of nodes and individual elements
    # this function creates a the linked list with the entered elements.
    def make_new_list(self, value):
        # nums = int(input("How many nodes do you want to create: "))
        # if nums == 0:
        #     return
        # for i in range(nums):
        #     value = int(input("Enter the value for the node:"))
        self.insert_at_end(value)

    # this function add an item at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def traverse_and_convert(self):
        converted_list = []
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                #
                converted_list.append(n.item)
                n = n.ref

            return converted_list
