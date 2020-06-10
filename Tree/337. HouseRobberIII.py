class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root))
    
    def helper(self, root):
        if not root:
            return (0,0)
        
        left, right = self.helper(root.left), self.helper(root.right)
        IsRob = root.val + left[1] + right[1] # when node is rob
        Not = max(left) + max(right)   # when node is not rob
        return (IsRob, Not)
