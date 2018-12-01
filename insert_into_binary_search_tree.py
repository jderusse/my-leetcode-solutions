# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        
        currentNode = root
        
        while 1:
            if val > currentNode.val:
                if currentNode.right == None:
                    currentNode.right = TreeNode(val)
                    break
                
                currentNode = currentNode.right
            else:
                if currentNode.left == None:
                    currentNode.left = TreeNode(val)
                    break
                
                currentNode = currentNode.left
        
        return root
        