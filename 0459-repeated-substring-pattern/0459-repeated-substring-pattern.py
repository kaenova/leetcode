class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (len(s) == 1):
            return False
        
        substring = ""
        
        for i in range(len(s) // 2):
            substring += s[i]
            data = s.split(substring)
            data = "".join(data)
            if len(data) == 0:
                return True
                
        return False
        
        