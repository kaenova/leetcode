import math

class Solution:
    number_to_letter_dict = {
        0: 'Z',
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H',
        9: 'I',
        10: 'J',
        11: 'K',
        12: 'L',
        13: 'M',
        14: 'N',
        15: 'O',
        16: 'P',
        17: 'Q',
        18: 'R',
        19: 'S',
        20: 'T',
        21: 'U',
        22: 'V',
        23: 'W',
        24: 'X',
        25: 'Y',
        26: 'Z'
    }
    
    def convertToTitle(self, columnNumber: int) -> str:
        original = columnNumber
        final_title = ""
        while columnNumber > 26:
            divide = columnNumber // 26
            reminder = columnNumber % 26
            final_title = self.number_to_letter_dict[reminder] + final_title
            if reminder == 0:
                columnNumber = divide - 1
            else:
                columnNumber = divide
        
        final_title = self.number_to_letter_dict[columnNumber] + final_title
        
        return final_title