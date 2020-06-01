class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # DFS
        if not root:
            return True
        # stack = deque()
        # stack.append((root, float('-inf'),float('inf')))
        # stack = [(root, float('-inf'),float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if root == None:
                continue
            
            if root.val <= lower or root.val >= upper:
                return False
            
            stack.append((root.left, lower, root.val))
            stack.append((root.right, root.val, upper))
            
        return True 
