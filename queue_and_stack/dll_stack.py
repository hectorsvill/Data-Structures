
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
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size


    def print_stack(self):
        head = self.storage.head
        while head:
            print(f"{head.value}", end=", ")
            head = head.next



if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.pop()
    s.push(2)
    s.print_stack()