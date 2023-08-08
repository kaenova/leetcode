class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cashier = {
            5: 0,
            10: 0,
            20: 0
        }
        
        for money in bills:
            if money == 5:
                pass
            elif money == 10:
                if cashier[5] > 0:
                    cashier[5] -= 1
                else:
                    return False
            elif money == 20:
                temp_money = money
                while temp_money > 5:
                        
                    if cashier[10] > 0 and temp_money - 10 >= 5:
                        temp_money = temp_money - 10
                        cashier[10] -= 1
                        continue
                        
                    if cashier[5] > 0 and temp_money - 5 >= 5:
                        temp_money = temp_money - 5
                        cashier[5] -= 1
                        continue
                        
                    return False
                    
            cashier[money] += 1
        
        return True