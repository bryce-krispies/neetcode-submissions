class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summation = len(nums)
        for i in range(len(nums)):
            summation += i - nums[i]
        return summation