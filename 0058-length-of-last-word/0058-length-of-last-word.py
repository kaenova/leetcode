class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        subword = ""
        
        found_space = False
        for char in s:
            if char == " ":
                found_space = True
                continue
            
            if char != " " and found_space:
                found_space = False
                subword = char
                continue
            
            subword += char
        
        return len(subword)
            
                