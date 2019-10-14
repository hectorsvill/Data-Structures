import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList



""" 
back                    front
Enqueue [0][1][2][3] Dequeue

"""

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # use dll because it allowes for asy filo
        self.storage = DoublyLinkedList()

    """Add item to the end of the queue
    """
    def enqueue(self, value):
        # add link to the back
        self.storage.add_to_head(value)
        # link added
        self.size += 1

    def dequeue(self):
        # link removed
        self.size -= 1

    def len(self):
        return self.size

    """ iterate through list and print """
    def print_queue(self):
        current = self.storage.head
        print(f"size: {self.size}")
        while current:
            print(current.value, end= ", ")
            current = current.next
        print("")

if __name__ == "__main__":
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)

    q.print_queue()

