# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


def LCA(root, p, q):
    if root == None:
        return None

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    if root == p or root == q:
        return root
    elif left and right:
        return root
    return left or right


LCA([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4)

# elif left:
#     return left
# elif right:
#     return right
# else:
#     return None

# array2tree()


class TreeNode():
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def array2tree(arr):
    q = deque()
    root = TreeNode(arr[0])
    q.append(root)

    idx = 1
    while idx < len(arr):
        cur_node = q.pop()

        # left Node
        if arr[idx] != 'null':
            cur_node.left = TreeNode(arr[idx])
            q.append(cur_node.left)
        idx += 1

        # right Node
        if arr[idx] != 'null':
            cur_node.right = TreeNode(arr[idx])
            q.append(cur_node.right)
        idx += 1
    return root


# private TreeNode fromArray(Integer[] arr) {
#         Deque<TreeNode> dq = new ArrayDeque<>();
#         int idx = 0;
#         TreeNode root = new TreeNode(arr[idx++]);
#         dq.add(root);
#         while (idx < arr.length) {
#             TreeNode node = dq.pop();
#             // Left node setup
#             if (arr[idx] != null) {
#                 node.left = new TreeNode(arr[idx]);
#                 dq.add(node.left);
#             }
#             idx++;
#             // Right node setup
#             if (idx < arr.length && arr[idx] != null) {
#                 node.right = new TreeNode(arr[idx]);
#                 dq.add(node.right);
#             }
#             idx++;
#         }
#         return root;
#     }
