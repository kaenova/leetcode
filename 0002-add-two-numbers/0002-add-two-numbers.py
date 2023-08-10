# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
       
    def onesTotal(self, ln1: Optional[ListNode], ln2: Optional[ListNode], reminder: int):
        val1 = 0 if ln1 is None else ln1.val
        val2 = 0 if ln2 is None else ln2.val

        total = val1 + val2 + reminder
        reminder = 0
        if total >= 10:
            reminder += 1
            total -= 10
        return total, reminder
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reminderVal = 0
        
        if l1 is None and l2 is None:
            return None
        elif l1 is None and l2 is not None:
            return l2
        elif l2 is None and l1 is not None:
            return l1
        
        # Init Calculation
        reminder = 0
        total, reminder = self.onesTotal(l1, l2, reminder)
        head = ListNode(total, None)
        
        # Pointer
        current = head
        cl1 = l1.next
        cl2 = l2.next
        
        while (cl1 is not None or cl2 is not None or reminder > 0 ):
            # Only reminder left
            if cl1 is None and cl2 is None and reminder > 0:
                current.next = ListNode(reminder, None)
                current = current.next
                reminder = 0
                break
            
            total, reminder = self.onesTotal(cl1, cl2, reminder)
            current.next = ListNode(total, None)
            
            current = current.next
            if cl1 is not None:
                cl1 = cl1.next
            if cl2 is not None:
                cl2 = cl2.next
        
        return head
            
            
            
            
            
            
            