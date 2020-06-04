# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        if not t1 and not t2:
            return None
        stack = deque()
        stack.append((t1))
        stack.append((t2))
        while stack:
            root1 = stack.popleft()
            root2 = stack.popleft()
            if root1 and root2:
                root1.val = root1.val + root2.val
                if not root1.left and root2.left:
                    root1.left = TreeNode(0)
                if not root1.right and root2.right:
                    root1.right = TreeNode(0)
                stack.append((root1.left))
                stack.append((root2.left))
                stack.append((root1.right))
                stack.append((root2.right))
        return t1
