# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        self.mem = None
        self.helper(root)
    
    def helper(self, root):
        if root:
            self.helper(root.right)
            self.helper(root.left)
            root.right = self.mem
            root.left = None
            self.mem = root
            
  # post-order
