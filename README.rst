- This project has three .py classes
    - node.py contains Node class to construct single node for single linked list
    - linkedlist.py contains SingleLinkedList class to build a linked list by appending elements at the end of the list
    - SingleLinkedList class also contains a function to traverse the linkedlist and convert it to an array
    - searchfromend.py has the main() block to trigger the process by prompting user to enter values for linkedlist and then to enter kth element
    - test_searchfromend.py has the unittests with assert statements testing the positives and exceptional cases

- To run code from searchfromend.py  , execute this command on cmd prompt after setting path to the project directory
    - python searchfromend.py

- To run unittests , execute this command on cmd prompt
    - python -m unittest discover <test_directory>

- Assumptions :
    - python version 3 or later is installed
    - pip setup
    - path environment variable is pointing to pip and python