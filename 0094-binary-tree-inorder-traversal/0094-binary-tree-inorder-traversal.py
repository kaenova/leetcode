# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [root.val]
        
        left = []
        right = []
        
        if root.left is not None:
            left = self.inorderTraversal(root.left)
        
        if root.right is not None:
            right = self.inorderTraversal(root.right)
        
        return left + [root.val] + right
