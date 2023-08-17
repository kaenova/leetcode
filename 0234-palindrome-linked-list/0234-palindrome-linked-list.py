# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        
        string = ""
        reversedString = ""
        
        currentHead = head
        while currentHead is not None:
            data = str(currentHead.val)
            string += data
            reversedString = data + reversedString
            currentHead = currentHead.next
            
        return string == reversedString