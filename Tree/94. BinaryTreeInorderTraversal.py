# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursively
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root, res)
        return res
    
    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)
            
    # iteratively
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        stack = deque()
        stack.append((root, False))
        while stack:
            root, flag = stack.pop()
            if root:
                if flag == False: #False
                    stack.append((root.right, False))
                    stack.append((root, True))
                    stack.append((root.left, False))
                else:
                    res.append(root.val)
        return res
