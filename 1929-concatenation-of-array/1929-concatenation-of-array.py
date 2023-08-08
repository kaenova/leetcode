class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums) * 2):
            idx = i % len(nums)
            res.append(nums[idx])
        return res