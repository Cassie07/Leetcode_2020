# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS(Iterative)
class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True
       
#         queue = deque()
#         queue.append((root.left, root.right))
#         while queue:
#             root_left, root_right = queue.popleft()
            
#             # test whether two nodes are None (This is symmetric)
#             if not root_left and not root_right:
#                 continue
            
#             # test whether one of two nodes is None (not symmetric)
#             if not root_left or not root_right:
#                 return False
                
#             if root_left.val != root_right.val:
#                 return False
                
#             queue.append((root_left.left, root_right.right))
#             queue.append((root_left.right, root_right.left)) 
#         return True

#   recursively(DFS)
    def isSymmetric(self, root):
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, l, r):
        if l and r:
            return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
        return l == r
