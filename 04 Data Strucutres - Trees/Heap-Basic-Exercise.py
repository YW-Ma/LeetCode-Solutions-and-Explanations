'''

Heap:
Two main properties:
    1. Compelete Binary Tree
    2. Heap Order Property
    
Index relationship: 
    Parent <--> Children 
    parent: n
         l-child: 2*n + 1
         r-child: 2*n + 2
    child: n
         parent: (n-1)//2

Insert and remove:
    1.
        insert at [next_index]
        remove [next_index - 1](last one)
    2.
        using heapify to guarantee the Heap Order Property

Use an array to represent a heap, and implement:
    1. insert (using up-heapify)   --> O(h) = O(logn), h is height of the tree, n is the number of nodes.
    2. remove (using down-heapify) --> O(h) = O(logn) 

'''


class Heap:
    def __init__(self, initial_size):
        '''
        create the CBT container for the heap using initial_size
        initialize the next_index with 0
        '''
        self.cbt = [0 for _ in range(initial_size)]
        self.next_index = 0
        
    def insert(self, data):
        '''
        insert the data into the cbt,
        up-heapify,
        update next_index,
        and then expand the cbt if next_index exceed the size.
        '''
    
    def remove(self):
        '''
        we want to remove the root value
        we can only remove the data in the next_index-1, so we need to swith the root and the leaf node at the next_index-1
        then, we decrease the next_index and down-heapify the heap from the root.
        during the down-heapify, we need to check if an index is valid before we use it.
        '''



# TEST:

heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('Inserted elements: {}'.format(elements))
# BANG
    
print('size of heap: {}'.format(heap.size()))
# BANG

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))
# BANG

print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print('Call is_empty: {}'.format(heap.is_empty()))