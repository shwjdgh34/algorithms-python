from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # DFS Preorder
    def serialize(self, root):
        rserialize = []
        def dfs_ser(root):
            rserialize.append(root.val if root else 'null')
            if not root:
                return 
            
            dfs_ser(root.left)
            dfs_ser(root.right)
        
        dfs_ser(root)
        
        return ','.join(rserialize)
           

        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        
        data_list = deque(data.split(','))
        
        def dfs_deser(data_list: deque):
            root = data_list.popleft()
            dfs_deser
            
        

        return 
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))