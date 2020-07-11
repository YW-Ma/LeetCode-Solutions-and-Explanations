'''
A Naive Solution: Brute Force: O(n^2)
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
1. Creat a dictionary to lookup whether an elements has been visited.
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

