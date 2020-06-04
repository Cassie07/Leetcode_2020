class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.best = 0
        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.best = max(self.best, L+R) 
            return max(L,R) + 1 # max(L,R) (previous) + 1(new)
        
        depth(root)
        return self.best
