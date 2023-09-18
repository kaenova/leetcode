# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root: TreeNode, currentSum: int, targetSum: int):
        total = root.val + currentSum
        has_children = (root.left is not None) or (root.right is not None)
        
        if (total == targetSum and not has_children):
            return True
        
        if not has_children:
            return False
        
        left_bool = False
        if root.left is not None:
            left_bool = self.helper(root.left, total, targetSum)
        
        right_bool = False
        if root.right is not None:
            right_bool = self.helper(root.right, total, targetSum)
        
        return left_bool or right_bool
        
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.helper(root, 0, targetSum)
