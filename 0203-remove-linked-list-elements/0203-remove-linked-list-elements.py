# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        pBefore = None
        pHead = head
        
        newListHead = None
        
        while pHead is not None:
            # If not same number
            if pHead.val != val:
                newNode = ListNode(pHead.val, None)
                if pBefore is None:
                    pBefore = newNode
                    newListHead = newNode
                else:
                    pBefore.next = newNode
                    pBefore = pBefore.next

            pHead = pHead.next
            
        return newListHead
        
        