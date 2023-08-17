# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def encodeLeft(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "None"
        
        left = "None" if root.left is None else str(root.left.val) + self.encodeLeft(root.left)
        right = "None" if root.right is None else str(root.right.val) + self.encodeLeft(root.right)
        
        return left+right
    
    def encodeRight(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "None"
        
        # We reversed form encodeLeft
        left = "None" if root.right is None else str(root.right.val) + self.encodeRight(root.right)
        right = "None" if root.left is None else str(root.left.val) + self.encodeRight(root.left)
        
        return left+right
    
        return "None"
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        if root.left is None and root.right is None:
            return True
        
        if (root.right is None and root.left is not None)\
        or (root.left is None and root.right is not None):
            return False
        
        if root.right.val != root.left.val:
            return False
        
        strLeft = self.encodeLeft(root.left)
        strRight = self.encodeRight(root.right)
        
        return strLeft == strRight