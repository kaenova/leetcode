# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depthRecursiveHelper(self,root: Optional[TreeNode], currentDepth: int) -> int:
        if root is None:
            return currentDepth - 1
        nextDepth = currentDepth + 1
        return max([self.depthRecursiveHelper(root.left, nextDepth), self.depthRecursiveHelper(root.right, nextDepth)])
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1
        nextDepth = depth + 1
        return max([self.depthRecursiveHelper(root.left, nextDepth), self.depthRecursiveHelper(root.right, nextDepth)])
        
        