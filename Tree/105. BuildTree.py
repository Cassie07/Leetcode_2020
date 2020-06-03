class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:   
        if inorder:
            root = TreeNode(preorder[0])
            index = inorder.index(root.val)
            root.left = self.buildTree(preorder[1:len(inorder[0:index+1])], inorder[0:index])
            root.right = self.buildTree(preorder[len(inorder[0:index+1]):], inorder[index+1:])
            return root
