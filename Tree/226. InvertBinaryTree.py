# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        res = root
        queue = deque()
        queue.append((root))
        while queue:
            root = queue.popleft()
            if root:
            # if not root: 
            #     continue
            # tmp = root.left
            # root.left = root.right
            # root.right = tmp
                root.left, root.right = root.right, root.left
                queue.append((root.left))
                queue.append((root.right))
        return res

 # DFS(recursively)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        if root:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.left, root.right = right, left
            return root
