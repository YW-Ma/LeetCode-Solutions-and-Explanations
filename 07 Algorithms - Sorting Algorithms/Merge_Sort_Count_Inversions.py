def count_inversions(arr):
    inversions, merged_arr = helper(arr)
    return inversions
    
def helper(arr):
    # Base case - do something to solve the most elementary inversion problem.[what is the base case?] - [和排序一样]
    # Divide arr into two parts
    # feed two parts into count_inversions, and get some kind of return value[what kind of return value?] [两个变量：逆序对 与 排好的array]
    # merged the return value in some way and return it.[in what way?] [left+right的逆序对，加上每次左边比右边当前大时的左侧剩余元素数]
    
    # base case:
    if len(arr) <= 1:
        return 0, arr # 0 - inversions, arr - sorted array
    # divide
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    left_inversions, left_sorted = helper(left)
    right_inversions, right_sorted = helper(right)
    
    # merge
    new_inversions, merged_arr = merge(left_sorted, right_sorted)
    new_inversions += left_inversions + right_inversions # plus the count of inversions that we find during the merging.
    return new_inversions, merged_arr

def merge(left, right):
    # merge two sorted subarray, and count the new inversions that we find during the merging
    merged = []
    left_index = 0
    right_index = 0
    inversions = 0 # count of inversions
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            inversions += len(left) - left_index
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    # concatenate the remaining part if any to the merged array
    merged += left[left_index:]
    merged += right[right_index:]
    
    return inversions, merged


# Testing
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")

arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)