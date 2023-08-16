# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # 0 0
        if p is None and q is None:
            return True
        
        # 0 1
        # 1 0
        if (p is not None and q is None) or (q is not None and p is None):
            return False
        
        # 1 1
        if (p is not None and q is not None) and (p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
#         # Check if it has "same" child node
#         reverse = str(p.left) == str(q.right) # Check if left of p is same in the right of q
        
#         if reverse:
#             # Compare the reversed child node
#             return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
#         else:
#             # Compare the same child node


"""
I was wrong that i handled reversed child lol

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # 0 0
        if p is None and q is None:
            return True
        
        # # 0 1
        # # 1 0
        # if (p is not None and q is None) or (q is not None and p is None):
        #     return False
        
        # 1 1
        if (p is not None and q is not None) and (p.val != q.val):
            return False
        
        # Check if it has "same" child node
        print(p)
        print(q)
        print("====")
        reverse = str(p.left) == str(q.right) # Check if left of p is same in the right of q
        
        if reverse:
            # Compare the reversed child node
            return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
        else:
            # Compare the same child node
            return self.isSameTree(p.left, q.left) and  self.isSameTree(p.right, q.right)
"""