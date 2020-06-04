# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        res = root
        stack = deque()
        stack.append((root))
        while stack:
            root = stack.popleft()
            if not root: 
                continue
            tmp = root.left
            root.left = root.right
            root.right = tmp
            stack.append((root.left))
            stack.append((root.right))
        return res
