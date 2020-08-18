'''
Heap sort:
1. convert an Array into a Max-Heap (using heap-insert)
2. get and remove the top value, and down-heapify the heap. (using heap-remove)

We can think that we build a priority queue, and pop the top value from the queue to realize the "heap sort"
'''

def arr_to_max_heap(arr):
    '''
    input - the original array
    output - the array representing a max-heap
    '''
    max_heap = arr
    for i in range(len(max_heap)):
        child_index = i
        parent_index = (i-1)//2
        while parent_index >= 0:
            child_value = max_heap[child_index]
            parent_value = max_heap[parent_index]
            if child_value <= parent_value:
                break
            else:
                max_heap[child_index] = parent_value
                max_heap[parent_index] = child_value
                child_index = parent_index
                parent_index = (child_index-1)//2
    return max_heap

def exchange_and_down_heapify(max_heap, end_index):
    '''
    exchange the top value with the element at end_index,
    down-heapify the heap from the new top value. (except the one in end_index)
    '''
    # exchange
    max_value = max_heap[0]
    last_value = max_heap[end_index]
    max_heap[end_index] = max_value
    max_heap[0] = last_value
    # down heapify
    parent_index = 0
    while parent_index <= end_index - 1: # while parent(current) is valid
        left_index = parent_index*2 + 1
        right_index = parent_index*2 + 2
        parent_value = max_heap[parent_index]
        left_value = None
        right_value = None
        # find the maximum of parent, left_child, and right_child(if they exist)
        maximum = parent_value
        if left_index <= end_index - 1: # left child exists
            left_value = max_heap[left_index]
            maximum = max(maximum, left_value)
        if right_index <= end_index - 1: # right child exists
            right_value = max_heap[right_index]
            maximum = max(maximum, right_value)
        
        # find out which one is the maximum:
        if left_value == maximum:
            # swap
            max_heap[left_index] = parent_value
            max_heap[parent_index] = left_value
            parent_index = left_index
        elif right_value == maximum:
            # swap
            max_heap[right_index] = parent_value
            max_heap[parent_index] = right_value
            parent_index = right_index
        else:
            # the new value is correctly placed
            return

def heap_sort(arr):
    if len(arr) <= 1:
        return arr
    # build a max-heap        
    max_heap = arr_to_max_heap(arr)
    # one by one extract elements
    end_index = len(max_heap) - 1
    while end_index > 0:
        exchange_and_down_heapify(max_heap, end_index)
        end_index -= 1
    return max_heap


# Testing
def test_function(test_case):
    result = heap_sort(test_case[0])
    if result == test_case[1]:
        print("Pass")
    else:
        print("False")

arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
test_case = [arr, solution]
test_function(test_case)


arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)


arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)


arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
test_case = [arr, solution]
test_function(test_case)