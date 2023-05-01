from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = TreeNode(value='A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.right = TreeNode('F')
root.left.left.left = TreeNode('G')
root.left.left.right = TreeNode('H')


def dfs(cur_node):
    if cur_node is None:
        return
    # visited? => 일방향이라서 방문표시 없어도 중복 방문 x
    dfs(cur_node.left)
    dfs(cur_node.right)


dfs(root)
