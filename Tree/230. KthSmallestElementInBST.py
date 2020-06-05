# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # iteratively
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        stack = deque()
        stack.append((root,False))
        while stack:
            root, flag = stack.pop()
            if root:
                if flag == False:
                    stack.append((root.right,False))
                    stack.append((root, True))
                    stack.append((root.left, False))
                else:
                    count += 1
                    if count == k:
                        return root.val

    # recursively
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.res = None
        self.k = k
        self.inorder(root)
        return self.res

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.count += 1
            if self.count == self.k:
                self.res = root.val
                return
            self.inorder(root.right)
