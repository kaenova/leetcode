class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numsSets = set(nums)
        numsDict = {}
        for i in nums:
            if i not in numsDict:
                numsDict[i] = 1
                continue
            numsDict[i] += 1
        
        for i in numsSets:
            if numsDict[i] == 1:
                return i
        return -1