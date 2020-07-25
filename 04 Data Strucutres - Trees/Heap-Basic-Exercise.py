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