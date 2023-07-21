class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        
        haystack_length = len(haystack)
        window_length = len(needle)
        
        high_head = window_length 
        low_head = high_head - window_length
        while (high_head <= haystack_length):
            if (haystack[low_head:high_head] == needle):
                return low_head
            
            high_head += 1 
            low_head = high_head - window_length

        return -1