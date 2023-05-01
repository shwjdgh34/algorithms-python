
from collections import deque

class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

root = TreeNode(value = 'A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.right = TreeNode('F')
root.left.left.left = TreeNode('G')
root.left.left.right = TreeNode('H')


def inorder(cur_node):
    if cur_node is None:
        return
    
    inorder(cur_node.left)
    print(cur_node.value)
    inorder(cur_node.right)

inorder(root)