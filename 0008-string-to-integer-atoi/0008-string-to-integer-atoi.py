class Solution:
    def myAtoi(self, s: str) -> int:
        number_dict = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        
        max_num = (2 ** 31) - 1
        min_num = - (2 ** 31)
        
        # string processing
        s = s.strip()
        
        def reset_ctx():
            is_minus = False
            base_10_multiplier = 1
            final_number = 0
            reset = False
            return is_minus, base_10_multiplier, final_number, reset
        
        is_minus, base_10_multiplier, final_number, reset = reset_ctx()

        head = len(s) - 1
        while head >= 0:
            current_char = s[head]
            
            if current_char == "-":
                is_minus = True
                head -= 1
                
                if reset:
                    is_minus, base_10_multiplier, final_number, reset = reset_ctx()
                reset = True
                continue
            
            if current_char == "+":
                is_minus = False
                head -= 1
                
                if reset:
                    is_minus, base_10_multiplier, final_number, reset = reset_ctx()
                reset = True
                continue
            
            if current_char not in number_dict:
                is_minus, base_10_multiplier, final_number, reset = reset_ctx()
                head -= 1
                continue
            
            # Resetting state
            if reset:
                is_minus, base_10_multiplier, final_number, reset = reset_ctx()
            
            final_number = final_number + number_dict[current_char] * base_10_multiplier
            base_10_multiplier *= 10
            head -= 1
        
        # Changinng to minus if true
        if is_minus:
            final_number *= -1
            
        # Clamping negative
        if final_number <= min_num:
            final_number = min_num
        
        # Clamping positive
        if final_number >= max_num:
            final_number = max_num
        
        return final_number