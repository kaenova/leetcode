class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        head_digits = len(digits) - 1
        if digits[head_digits] < 9:
            digits[head_digits] += 1
            return digits
        
        reminder = True
        while (reminder):
            digits[head_digits] = 0
            head_digits -= 1
            
            if (head_digits == -1):
                digits.insert(0, 0)
                head_digits = 0
            
            digits[head_digits] += 1
            
            if digits[head_digits] <= 9:
                return digits
        