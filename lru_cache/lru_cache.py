import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


""" LRU
Least Recently Used

LRU, limit=4-> [0][1][2]

get 1          bottom       top
LRU, limit=4-> [0][2] [1]

set 3
LRU, limit=4-> [0][2][1][3]

get 0
-get zero and move zero to top
LRU, limit=4-> [2][1][3][0]

set 4
remove 0 and set 4
LRU, limit=4-> [2][1][3][4]

"""
""" LRU Cache

"""



class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return


        if self.size == self.limit:
            del self.storage[self.order.remove_from_head()[0]]
            self.size -= 1

        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1



if __name__ == "__main__":
    lru = LRUCache(limit=3)
    # 
    # lru.set('item1', 'a')
    # lru.set('item2', 'b')
    # lru.set('item3', 'c')
    #
    # x = lru.get('item11')
    # print(x)
    # print(lru.storage)
    # lru.set('item2', 'z')
    #
    # print(lru.storage)
    #
