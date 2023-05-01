from collections import deque


# level order
def maxDepth(root):
    if root is None:
        return 0
    q = deque()
    level = 1
    max_depth = 0
    q.append((root, level))
    while q:
        cur_node, cur_level = q.popleft()
        max_depth = max(max_depth, cur_level)
        if cur_node.left:
            q.append(cur_node.left, cur_level + 1)
        if cur_node.right:
            q.append(cur_node.right, cur_level + 1)

    return max_depth


# recursion - postorder


class TreeNode:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v


root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

print(maxDepth(root))


def maxDepth(root):
    max_depth = 0

    if root is None:
        return max_depth

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    max_depth = max(left_depth, right_depth) + 1
    return max_depth


maxDepth(root)
