import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


""" 

back [0][1][2][3] front

"""

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # use dll because it allowes for asy filo
        self.storage = ListNode(None)

    """Add item to the end of the queue
    """
    def enqueue(self, value):
        if self.size == 0:
            # first link
            self.storage = ListNode(value)
        else:
            # add to the front
            self.storage = self.storage.add_to_head(value)


        # link added
        self.size += 1

        
    def dequeue(self):

        # link removed
        self.size -= 1

    def len(self):
        return self.size


q = Queue()

# print(q.size)