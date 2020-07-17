# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        res = root
        self.sums = 0
        self.right_first(root)
        return res
    
    def right_first(self, root):
        if root:
            self.right_first(root.right)
            root.val += self.sums
            self.sums = root.val
            self.right_first(root.left)
