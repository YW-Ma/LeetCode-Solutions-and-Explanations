def quicksort(items):
    quick_sort(items,0,len(items)-1)

def quick_sort(items, begin, end): 
    '''
    divide, recursivly call itself, determine the base case
    '''
    # base case:
    if begin > end:
        return
    # partition - according to the pivot.
    pivot = partition(items, begin, end)
    # divide
    quick_sort(items, begin, pivot - 1)
    quick_sort(items, pivot + 1, end)

def partition(items, begin, end): 
    '''
    conquer,
    reorder the array so that all elements with 
    values less than the pivot come before the pivot

    return value --> the current index of the pivot
    '''
    left_index = begin
    pivot_index = end
    pivot_value = items[pivot_index] # 由于pivot的值不变，所以没必要每个loop重新获得。 The pivot_value remain unchanged during the while-loop.
    while left_index < pivot_index:
        left_value = items[left_index]
        if left_value <= pivot_value:
            left_index += 1
            continue
        else:
            items[left_index] = items[pivot_index - 1]
            items[pivot_index - 1] = pivot_value
            items[pivot_index] = left_value
            pivot_index -= 1
    
    return pivot_index


# Testing
items = [8, 3, 1, 7, 0, 10, 2]
quicksort(items)
print(items)

items = [1, 0]
quicksort(items)
print(items)

items = [96, 97, 98]
quicksort(items)
print(items)