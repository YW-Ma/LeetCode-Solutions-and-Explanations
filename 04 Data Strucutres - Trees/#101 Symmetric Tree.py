# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The link to this problem: https://leetcode.com/problems/symmetric-tree/


'''
solution 1， based on DFS

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        t1 = root.left
        t2 = root.right
        
        def isMirror(t1,t2):
            # base case:
            if t1 is None and t2 is None:
                return True
            elif t1 is None and t2 is not None:
                return False
            elif t1 is not None and t2 is None:
                return False
            # elif t1 is not None and t2 is not None:
            return (t1.val == t2.val) and (isMirror(t1.left, t2.right)) and (isMirror(t1.right, t2.left))
        
        return isMirror(t1, t2)

'''

'''
Solution 2, based on BFS

'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        t1 = root.left
        t2 = root.right
        q = []
        q.insert(0,t1)
        q.insert(0,t2)
        while len(q) > 0:
            t1 = q.pop()
            t2 = q.pop()
            if t1 is None and t2 is None:
                continue
            elif t1 is None or t2 is None:
                return False
            elif t1.val != t2.val:
                return False
            q.insert(0,t1.left)
            q.insert(0,t2.right)
            q.insert(0,t1.right)
            q.insert(0,t2.left)
        
        return True
        

        
        
        
        
        
        
        
        
        
        
        