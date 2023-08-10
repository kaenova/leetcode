# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  
    
    def appendCurrentList(self, val, finalList, currentList):
        if finalList is None:
            finalList = ListNode(val, None)
            currentList = finalList
        else:
            currentList.next = ListNode(val, None)
            currentList = currentList.next
        return finalList, currentList

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashMap = {
            # val : num_occur
        }
        
        while head is not None:
            if head.val not in hashMap:
                hashMap[head.val] = 0
            hashMap[head.val] += 1
            head = head.next
        
        finalList = None
        currentList = finalList
        
        for i in hashMap:
            if hashMap[i] == 1:
                finalList, currentList = self.appendCurrentList(i, finalList, currentList) 
            
        return finalList
        
        