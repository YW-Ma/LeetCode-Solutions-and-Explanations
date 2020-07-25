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

本次出现的问题：
    1. remove的时候，size为0的时候，remove依然会返回0位置上的值。
    这是因为没有对next_index进行检查，导致获得了一个在逻辑上已经被删掉了的值。

'''


class Heap:
    def __init__(self, initial_size):
        '''
        create the CBT container for the heap using initial_size
        initialize the next_index with 0
        '''
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0
        
    def insert(self, data):
        '''
        insert the data into the cbt,
        up-heapify,
        update next_index,
        and then expand the cbt if next_index exceed the size.
        '''
        # insert
        if self.next_index >= len(self.cbt):
            print(f"Index {self.next_index}Exceed the limitation of the CBT {len(self.cbt)}")
            return
        self.cbt[self.next_index] = data
        self.next_index += 1
        
        # up-heapify
        self._up_heapify()
        
        # expand the cbt if necessary
        if self.next_index >= len(self.cbt):
            new_cbt = [None for _ in range(2*len(self.cbt))]
            for i in range(len(self.cbt)):
                new_cbt[i] = self.cbt[i]
            self.cbt = new_cbt
    
    def remove(self):
        '''
        we want to remove the root value
        we can only remove the data in the next_index-1, so we need to swith the root and the leaf node at the next_index-1
        then, we decrease the next_index and down-heapify the heap from the root.
        during the down-heapify, we need to check if an index is valid before we use it.
        '''
        if self.size() == 0:
            return None # otherwise, in down_heapify, we will get the value loacted in 0 index.
        
        # remove the root value by overwriting the root value with the last one.
        root_value = self.cbt[0] # 可能不存在root,用之前要先check
        self.cbt[0] = self.cbt[self.next_index - 1]
        # down heapify
        self._down_heapify()
        # return root value
        self.next_index -= 1
        return root_value
        
    def _up_heapify(self):
        '''
        An internal function.
        From the newly added node, 
        switch the node with its parent until the parent is smaller than the node.
        or the node doesn't have a parent. (i.e. index < 1)
        '''
        # obtaining the index and element
        child_index = self.next_index - 1
        parent_index = (child_index - 1)//2
        
        while parent_index >= 0:
            child_element = self.cbt[child_index]
            parent_element = self.cbt[parent_index]
            # comparing
            if child_element >= parent_element:
                return
            # switching
            self.cbt[parent_index] = child_element
            self.cbt[child_index] = parent_element
            child_index = parent_index
            # updating indices and elements
            parent_index = (child_index - 1)//2
    
    def _down_heapify(self):
        '''
        An internal function.
        From the root,
        switch the node with its smaller child until the smaller child is larger than the node.
        or the node doesn't have a child.
        Please valid the indices of both children before visiting them in the CBT.
        '''
        parent_index = 0

        while parent_index < self.next_index:
            # calculating new indices
            left_child_index = 2*parent_index + 1
            right_child_index = 2*parent_index + 2     
            
            # validation and comparing --> find out the minimum
            parent_element = self.cbt[parent_index]
            minimum = parent_element
            
            if left_child_index < self.next_index:
                left_child_element = self.cbt[left_child_index]
                minimum = min(left_child_element, parent_element)
                
            if right_child_index < self.next_index:
                right_child_element = self.cbt[right_child_index]
                minimum = min(right_child_element, minimum)
            
            # switching
            if parent_element == minimum:
                return
            elif left_child_element == minimum:
                self.cbt[left_child_index] = parent_element
                self.cbt[parent_index] = left_child_element
                parent_index = left_child_index
            elif right_child_element == minimum:
                self.cbt[right_child_index] = parent_element
                self.cbt[parent_index] = right_child_element
                parent_index = right_child_index
        
        return
        
    def size(self):
        return self.next_index
    
    def get_minimum(self):
        '''
        peek
        '''
        return self.cbt[0] 
    
    def is_empty(self):
        return self.next_index == 0
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