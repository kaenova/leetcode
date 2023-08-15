class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return (nums[0] + nums[1]) % 10
        
        newArr = []
        for i in range(1, len(nums)):
            newArr.append(nums[i - 1] + nums[i] % 10)
            
        return self.triangularSum(newArr)