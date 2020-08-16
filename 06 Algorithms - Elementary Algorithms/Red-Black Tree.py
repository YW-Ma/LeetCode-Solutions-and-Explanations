# -*- coding: utf-8 -*-
'''
rules:
    1.All nodes have a color
    2.All nodes have two children (use NULL nodes)
        All NULL nodes are colored black
    3.If a node is red, its children must be black
    4.The root node must be black (optional)
    5.Every path to its descendant NULL nodes must contain the same number of black nodes
'''
# 树的Node
class Node(object):
    def __init__(self, value, parent, color):
        # 创建默认Node的值
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color
    def __repr__(self):
        color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, color)


# 两个工具函数
def grandparent(node):
    # 获得grandparent，但是留心node.parent可能就已经是空的。
    if node.parent == None:
        return None
    return node.parent.parent

def pibling(node):
    # 返回parent的sibling（三种情况）
    p = node.parent #可能为空
    gp = grandparent(node) #可能为空
    if gp == None:
        return None
    elif p == gp.left:
        return gp.right
    elif p == gp.right:
        return gp.left
    

# 红黑树的逻辑
class RedBlackTree(object):
    def __init__(self, root):
        # 创建根节点
        self.root = Node(root, None, 'red')
    
    def insert(self, new_val):
        # 按照BST要求插入new_val
        # 按照red-black tree的rule来进行rebalance
        new_node = self._insert_helper(self.root, new_val) #单纯的BST不需要这个返回值，但是红黑树需要它来rebalance
        self.rebalance(new_node)
        return new_node
    
    def _insert_helper(self, current, new_val):
        # 递归地调用，如果能在自己这里插入就插入，不然把任务留给下一层。
        # 还需要返回插入后的node以进行rebalance，所以要递归地传递这个插入后的node。
        if current.value < new_val:
            if current.right:
                return self._insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                return self._insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left
        
    def rebalance(self, node):
        # 分析node处于5种case中的哪一种，并进行rebalance。
        # CASE 1 - New node is root
        # CASE 2 - Parent is black
        # CASE 3 - Parent is red, and parent's sibling is red.
        # CASE 4 - Parent is red, and parent's sibling is black. Inside.
        # CASE 5 - Parent is red, and parent's sibling is black. Outside.
        
        # CASE 1 & 2
        if node.parent == None:
            return
        if node.parent.color == 'black':
            return
        
        # CASE 3 (此后，parent.color肯定是red，因为black的话走CASE 2)
        if pibling(node) and pibling(node).color == 'red': # parent's color must be red now.
            # P -> black, Pibling -> black
            # GP -> red, as a newly inserted node.(rebalance it)
            node.parent.color = 'black'
            pibling(node).color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))
        
        # CASE 4 (inside) The newly inserted node has a red parent, but that parent has a black sibling
        # 需要通过左旋或右旋变为CASE 5，即outside（node和parent都是同类孩子）。
        # 如果自己(node)是一个左孩子，parent是一个右孩子，那么从parent右旋（都右）
        # 如果自己(node)是一个右孩子，parent是一个左孩子，那么从parent左旋（都左）
        # 当前node已经不是“新插入”的位置了，要走到node.left或right以变成CASE 5
        gp = grandparent(node)
        if gp == None: # 如果没有gp，不需要进行后续步骤。
            return
        if gp.left and gp.left.right == node:#左孩子的右孩子
            self.rotate_left(node.parent)
            # 漏了一步！ - 还要向下走到node.left才能变成CASE 5
            node = node.left
        elif gp.right and gp.right.left == node:
            self.rotate_right(node.parent)
            node = node.right
        
        # CASE 5 - (outside) The newly inserted node has a red parent, but that parent has a black sibling
        # 如果node是左孩子（此时parent也是左孩子），那么从gp右旋，反之左旋。
        # 为了满足rule 5，修改原gp为红，原parent为black
        # 注意，要重新获取一次parent和gp
        p = node.parent
        gp = p.parent
        
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        gp.color = 'red' #由于parent是black，所以省略了rebalance
        p.color = 'black'
        
        
    def rotate_right(self, node):
        # 预备：把node左孩子的右孩子作为node的左孩子
        # 旋转：把node贴在node的左孩子的右孩子上面（包括两个操作）
        # 拼接：把node的左孩子接在node的parent上面（包括两个操作）（左、右两种情况）
        p = node.parent
        node_up = node.left
        node.left = node_up.right
        
        node_up.right = node
        node.parent = node_up
        
        if p:
            if node == p.left:
                p.left = node_up
            if node == p.right:
                p.right = node_up
        node_up.parent = p #可能为None

    def rotate_left(self, node):
        p = node.parent
        node_up = node.right
        node.right = node_up.left
        
        node_up.left = node
        node.parent = node_up
        
        if p:
            if node == p.left:
                p.left = node_up
            if node == p.right:
                p.right = node_up
        node_up.parent = p #可能为None
        
        
# Testing:
def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)
        
print('CASE 1/2')
tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)

print_tree(tree.root)

print('CASE 3')
tree.insert(13)
print_tree(tree.root)

print('CASE 4/5')
tree.insert(16)
print_tree(tree.root)

        
        
        