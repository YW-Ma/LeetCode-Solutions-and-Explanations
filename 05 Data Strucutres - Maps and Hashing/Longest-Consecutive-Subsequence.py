'''
A Naive Solution: Brute Force: O(n^2). n is the length of the input_list
'''
def longest_consecutive_subsequence(input_list):
    longest_streak = -1
    longest_subsequence = []
    
    for element in input_list:
        temp_streak = 1
        temp_subsequence = [element]
        
        while element + 1 in input_list:
            temp_streak += 1
            temp_subsequence.append(element + 1)
            element = element + 1
        
        if temp_streak > longest_streak:
            longest_streak = temp_streak
            longest_subsequence = temp_subsequence
        
    return longest_subsequence

'''
A Solution with HashMap: O(n)
---------------------------------------------------------------------------
1. Creat a dictionary to lookup whether an elements is existed(xxx in dict) and visited(dict[xxx]>=0).
key --> the elements in the list
value --> the corresponding index [will change to -1 after visiting]
---------------------------------------------------------------------------
2. For each element in the input_list, first mark it as visited in dictionary
2.2 check in forward direction. visit all consecutive elements if any.
2.3 check in backward direction. visit all consecutive elements if any.
2.4 keep a track of the [length of longest subsequence] visited so far. 
	also store the [index of the beginning element] corresponding to this subsequence.
---
e.g. if the input is [100,4,200,1,3,2,5,6], the value of 4,1,3,2,5,6 will change to -1
	 after visiting the 4.
	 the value of 5,6 change to -1 in 2.2
	 the value of 1,2,3 change to -1 in 2.3

	 此外，可以用set来实现单方向的查找, 从 value - 1 不在set里的元素开始正序追加即可。
	 用单一一个dict，则无法实现单向查找，因为4已经标记5、6为visited，在遇到1的时候就不知道是不是该访问一下5、6
---------------------------------------------------------------------------
3. return a new list starting 
	from [index of the beginning element] 
	to [index of the beginning element] + [length of lengest subsequence]
---------------------------------------------------------------------------
'''
def longest_consecutive_subsequence(input_list):
    '''
    1.
    create a dictionary storing <element, index>
    once an element is visited, change the index into -1
    '''
    element_dict = {}
    for index, value in enumerate(input_list):
        element_dict[value] = index
    
    max_length = -1 # the max length of consecutive subsequence
    starting = -1  # where the subsequence with longest length starts
    
    '''
    2. 
    For each element in the input_list, first mark it as visited in dictionary
    and then check in forward and backward direction to visit all consecutive elements of it.
    '''
    for index, element in enumerate(input_list):
        
        current_length = 1
        current_starting = index
        
        current = element
        element_dict[element] = -1 # visited
        
        # check in forward direction
        current = element + 1
        '''
        key differences:
            while current in element_dict and element_dict[current] >= 0: O(1)
            while current in input_list and element_dict[current] >= 0:   O(n)
        '''
        while current in element_dict and element_dict[current] >= 0:
            current_length += 1        # record
            element_dict[current] = -1 # visited
            current = current + 1      # move
        
        # check in backward direction
        current = element - 1
        while current in element_dict and element_dict[current] >= 0:
            current_length += 1        # record
            current_starting = element_dict[current] # record
            element_dict[current] = -1 # visited
            current = current - 1      # move
        
        if current_length >= max_length:
            if current_length == max_length and current_starting > starting:
                continue
            # update when: 1. longer, 2. length is the same but start earlier
            starting = current_starting
            max_length = current_length
    '''
    3. 
    return a new list starting 
	from [index of the beginning element] 
	to [index of the beginning element] + [length of lengest subsequence]
    '''
    start_element = input_list[starting]
    return [i for i in range(start_element, start_element + max_length)]
