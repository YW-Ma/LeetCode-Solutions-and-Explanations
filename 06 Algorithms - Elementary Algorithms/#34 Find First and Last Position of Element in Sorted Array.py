def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary 
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """
        
    # TODO: Write your first_and_last function here
    # Note that you may want to write helper functions to find the start 
    # index and the end index
    first_index = find_first_index(arr, number, 0, len(arr) - 1)
    last_index = find_last_index(arr, number, 0, len(arr) - 1)
    return [first_index, last_index]
       
    
def find_first_index(arr, number, start, end):
    # 我们的逻辑在 start<=end 时才展开，如果不符合逻辑，要先剥离
    if start > end:
        return -1
    # 要想知道“子串里有没有number” 可以用返回值是不是-1来判断。
    
    mid = (start + end) // 2
    if arr[mid] == number:
        # 与普通的BS不一样，要继续找到最左侧开头，而且用BS来找而不是用简单的迭代来找。
        # “还能找到更左侧的吗？”
        response = find_first_index(arr, number, start, mid - 1)
        # “找不到啦！” --> “所以当前这个就是最左的”
        if response == -1:
            return mid
        # “收到了更深层的信号！” --> “负责传递信号即可”
        elif response != 1:
            return response
    
    elif arr[mid] > number:
        # 太大啦，在左侧（更小）找一个相等的元素
        return find_first_index(arr, number, start, mid - 1)
    
    elif arr[mid] < number:
        # 太小啦，在右侧找一个相等的元素
        return find_first_index(arr, number, mid + 1, end)
    
    
    
def find_last_index(arr, number, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2    
    if arr[mid] == number:
        # “还能找到更右侧的吗？”
        response = find_last_index(arr, number, mid + 1, end)
        # “找不到啦！” --> “所以当前这个就是最右侧的”
        if response == -1:
            return mid
        # “收到了更深层的信号！” --> “负责传递信号即可”
        elif response != 1:
            return response
    
    elif arr[mid] > number:
        # 太大啦，在左侧（更小）找一个相等的元素
        return find_last_index(arr, number, start, mid - 1)
    
    elif arr[mid] < number:
        # 太小啦，在右侧找一个相等的元素
        return find_last_index(arr, number, mid + 1, end)




def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)


input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)