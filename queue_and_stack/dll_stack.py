
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


""" Stack
push 1
stack ---> [1] 

push 2
stack ---> [1][2]

push 3
stack ---> [1][2][3]

pop
stack ---> [1][2]


pop
stack ---> [1]

"""


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        pass

    def pop(self):
        pass

    def len(self):
        pass
