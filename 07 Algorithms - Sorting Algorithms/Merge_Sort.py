def mergesort(items):
    # Divide - 1/2 base case
    if len(items) <= 1:
        return items
    # Divide - 2/2 Divide work
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left_sorted = mergesort(left)
    right_sorted = mergesort(right)
    
    # Conquer - solve a easy problem (not a smaller problem)
    return merge(left_sorted, right_sorted)
    
def merge(left, right):
    # 1. 变量声明（存到merged里面）
    merged = []
    left_index = 0
    right_index = 0
    # 遍历数组直到有一个数组元素被耗尽
    while left_index < len(left) and right_index < len(right):
        # 如果左边比右边当前元素大，则在merged后append右边的当前元素（小到大排序）
        # 并且记得增加右侧index的值
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # 反之，在merged后append左侧的当前元素，并增加左侧index的值
        else:
            merged.append(left[left_index])
            left_index += 1
    # 从循环中退出后，将余下的array连接到merged上。
    # 这是因为：至少有一个是空的，而另一个里剩下的部分：
    # a) 已经是排好序的（有序）
    # b) 都排在merged当前的最后一个元素的后面（更大）
    merged += left[left_index:]
    merged += right[right_index:]
    # 返回merged
    return merged


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))