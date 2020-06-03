# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        layer = 1
        queue = deque()
        queue.append((root, layer))
        while queue:
            root, layer = queue.popleft()
            if root:
                res = self.add_to_res(res, layer, root.val)
                queue.append((root.left, layer + 1))
                queue.append((root.right, layer + 1))
        return res
    
    def add_to_res(self, res, layer, value):
        if layer <= len(res):
            res[layer-1].append(value)
        else:
            res.append([value])
        return res
