# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        self.sum = sum
        self.dfs(root)
        return self.count
    
    def dfs(self, root):
        if root:
            self.test(root, self.sum)
            self.dfs(root.left)
            self.dfs(root.right)
    
    def test(self, root, target):
        if root:
            if root.val == target:
                self.count += 1
            
            self.test(root.left, target - root.val)
            self.test(root.right, target - root.val)
