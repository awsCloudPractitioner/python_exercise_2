from linkedlist import SingleLinkedList

# Python does not have pre-defined data type for Linked List
# Created two custom python classes as Node and Single Linked List to provide an implementation of such a data type.

# Series of steps involved to implement the requirement are -
# Build a single linked list by prompting user to enter values
# Traverse the list
# Convert the linked list to an array (this is to abide by the requirement which says linked list can be walked once,
# reverse, length or size cannot be used)


# class SearchFromEnd:

def kth_element_from_end(converted_list, k):
    return converted_list[-k]


if __name__ == '__main__':

    new_linked_list = SingleLinkedList()

    nums = int(input("How many nodes do you want to create: "))
    if nums <= 0:
        raise ValueError("Invalid number of nodes..")

    for i in range(nums):
        value = int(input("Enter the value for the node:"))
        new_linked_list.make_new_list(value)

    # get list from linked list
    converted_array = new_linked_list.traverse_and_convert()

    kth_value = int(input("Enter the kth value to be returned from the end:"))
    print(kth_element_from_end(converted_array, kth_value))



