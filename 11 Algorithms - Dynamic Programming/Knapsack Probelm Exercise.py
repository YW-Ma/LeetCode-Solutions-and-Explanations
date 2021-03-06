'''
Knapsack Problem

Assume you are given two things:
- The items, each having its associated weight (kg) and value ( $ ).
- A knapsack that can hold a maximum weight of knapsack_max_weight (kg).

Implement the function knapsack_max_value() to return the maximum total value 
of items that can be accommodated into the given knapsack.
'''

# Helper code
import collections
# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])

'''
Naive Approach 错误思路示例：
Naive Approach (Brute Force)
- Base case: 指定物体不存在 or 空间不够放指定的物体
- Divide:
    1. 放置当前物体。计算valueA = 当前指定物体的价值 + 递归计算剩余空间最大值（指定放置下一个物体）
    2. 不放置当前物体。计算valueB = 递归计算当前空间最大值（指定放置下一个物体）
- Return:
    valueA、valueB的最大值

问题：指定物体A放的下。放了A后，A+1放不下，但A+2放的下。
在本方案中，A+1放不下后直接让valueA为0了，这是不行的。
           放置A 与 A+2 的情况，是放置A的子集(valueA)，不是不放置A的子集（valueB）
           要把递归树想清楚，不要漏了情况。
'''
def knapsack_max_value_brute_force_wrong(knapsack_max_weight, items):
    return knapsack_recursive_wrong(knapsack_max_weight, items, 0)

def knapsack_recursive_wrong(capacity, items, index):
    # base case
    if (index > len(items) - 1) or (capacity < items[index].weight) : 
        return 0
    # Put the last item into the bag
    valueA = items[index].value + knapsack_recursive(capacity - items[index].weight, items, index + 1)
    # or not put the last item into the bag
    valueB = knapsack_recursive(capacity, items, index + 1)
    # find the biggest value for the two aforementioned situations
    return max(valueA, valueB)


'''
Naive Approach 正确思路示例：
Naive Approach (Brute Force)
- Base case: 指定物体不存在 or 空间不存在
- Divide:
    1. 放置当前物体。
        如果够放置当前物体，则计算valueA = 当前指定物体的价值 + 递归计算剩余空间最大值（指定放置下一个物体）
        否则valueA = 0 （放置当前物体下的两类分支情况）
    2. 不放置当前物体。计算valueB = 递归计算当前空间最大值（指定放置下一个物体）
- Return:
    valueA、valueB的最大值
time complexity O(2^n), where n is the number of given items, because we calculate
both the two options (put or not put) for each given item.
'''
def knapsack_max_value_brute_force(knapsack_max_weight, items):
    return knapsack_recursive(knapsack_max_weight, items, 0)

def knapsack_recursive(capacity, items, index):
    # base case
    if (index > len(items) - 1) or (capacity <= 0) : 
        return 0
    # Put the last item into the bag
    if capacity >= items[index].weight:
        valueA = items[index].value + knapsack_recursive(capacity - items[index].weight, items, index + 1)
    else:
        valueA = 0
    # or not put the last item into the bag
    valueB = knapsack_recursive(capacity, items, index + 1)
    # find the biggest value for the two aforementioned situations
    return max(valueA, valueB)

'''
Dynamic Programming Approach (Brute Force)
------------------------------------
- capacity : 0  1  2  3  4  5  ...
- max_value: 0  0  0  0  0  0 
------------------------------------
lookup table 查找表：储存中间结果 以进行重用
一开始，查找表value都是0
随后，一件件取出物体，按照下列规则更新各个能容纳它的capacity的value：
规则：如果此物体的价值 + 剩余capacity在表中的value > 原value，则更新为新value。
'''

# DP Solution
# Get the maximum total value ($) of items that can be accommodated into the given knapsack
def knapsack_max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    # Initialize a lookup table to store the maximum value for each capacity
    lookup_table = [0 for _ in range(knapsack_max_weight + 1)]
    
    # Iterate down the given item-list
    for item in items:
        
        # The "capacity" represents amount of remaning capacity of knapsack at a given moment
        for capacity in reversed(range(knapsack_max_weight + 1)): 
            # 关键在于reversed() 如果不reverse，会出现把同一个物体使用多次的情况
            
            if item.weight <= capacity:
                valueA = lookup_table[capacity]
                valueB = lookup_table[capacity - item.weight] + item.value
                lookup_table[capacity] = max(valueA, valueB)
    
    return lookup_table[knapsack_max_weight]

# Test:

tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    
    print(knapsack_max_value_brute_force(**test['input']))
    assert test['correct_output'] == knapsack_max_value_brute_force(**test['input'])  
    
    print(knapsack_max_value(**test['input']))
    assert test['correct_output'] == knapsack_max_value(**test['input'])  