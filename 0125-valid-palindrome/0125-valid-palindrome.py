class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        # Getting valid character
        newS = ""
        reversedS = ""
        for x in s:
            if x in "abcdefghijklmnopqrstuvwxyz0123456789":
                newS += x
                reversedS = x + reversedS
        
        return newS == reversedS