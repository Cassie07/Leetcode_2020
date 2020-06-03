class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res_depth = 1
        stack = deque()
        stack.append((root, 1, False))
        while stack:
            root, depth, flag = stack.pop()
            if root:
                if flag == False:
                    stack.append((root.left, depth+1, False))
                    stack.append((root, depth, True))
                    stack.append((root.right, depth+1, False))
                else:
                    if depth > res_depth:
                        res_depth = depth             
        return res_depth
