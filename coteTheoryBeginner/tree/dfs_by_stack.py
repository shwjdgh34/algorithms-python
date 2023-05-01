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



def dfs(root):
    visited = []
    if root is None:
        return 0;
    s = []
    s.append(root)
    while s != []:
        cur_node = s.pop()
        visited.append(cur_node.value)
        if cur_node.right:
            s.append(cur_node.right)
        if cur_node.left:
            s.append(cur_node.left)    
    return visited

dfs(root)
