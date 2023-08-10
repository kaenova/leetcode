# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        currentOriginal = head.next

        headNode = ListNode(head.val, None)
        currentDuplicate = headNode
        
        while currentOriginal is not None:
            if currentOriginal.val != currentDuplicate.val:
                currentDuplicate.next = ListNode(currentOriginal.val, None)
                currentDuplicate = currentDuplicate.next
            
            currentOriginal = currentOriginal.next
        
        return headNode
        
        
        