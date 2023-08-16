class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        allJewels = set(jewels)
        for stone in stones:
            if stone in allJewels:
                count += 1
        
        return count