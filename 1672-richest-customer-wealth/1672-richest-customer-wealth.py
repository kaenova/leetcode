class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max([sum(x) for x in accounts])
        
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_w = sum(accounts[0])
        for x in accounts:
            if (sum(x) >= max_w):
                max_w = sum(x)
        return max_w
        
        