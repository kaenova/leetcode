# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        h1 = head
        h2 = head
        
        while h2 is not None:
            h1 = h1.next
            
            if h2.next is None:
                return False
            h2 = h2.next
            if h2.next is None:
                return False
            h2 = h2.next
            
            if h1 == h2:
                return True
            
        
        return False
        