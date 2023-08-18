# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def counterSecondMiddleFromWholeCounter(self, counter: int) -> int:
        if counter % 2 == 0:
            return counter // 2 + 1
        else:
            return math.ceil(counter / 2)
        
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        counterFront, counterMiddle = 1, 1
        currentHead, middleHead = head, head
        beforeMiddleHead = None
        
        while currentHead is not None:
            # Move the middle head
            while counterMiddle != self.counterSecondMiddleFromWholeCounter(counterFront):
                beforeMiddleHead = middleHead
                middleHead = middleHead.next
                counterMiddle += 1 
            
            # Move the front head
            currentHead = currentHead.next
            counterFront += 1
        
        if counterFront == 2:
            return None
        
        beforeMiddleHead.next = middleHead.next
        
        return head