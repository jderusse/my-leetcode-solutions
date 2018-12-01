# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        node = root
        
        while 1:
            if node == None:
                return None
        
            if node.val == val:
                return node
            
            if val > node.val:
                node = node.right
            else:
                node = node.left