# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        h0 = ListNode(head.val)
        h1 = head.next
        while h1 is not None:
            # Preparing for next interation
            h2 = h1.next
            
            newHead = ListNode(h1.val, h0)
            h0 = newHead
            
            # Next iteration
            h1 = h2
            
        
        return h0
