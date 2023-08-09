# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (list2 is None and list1 is not None):
            return list1
        
        if (list1 is None and list2 is not None):
            return list2
        
        if (list1 is not None and list2 is not None):
            if (list2.val <= list1.val):
                return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
            else:
                return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        
        return None
        
        
        