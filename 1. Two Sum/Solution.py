class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in nums[i+1:]:
                return [i, nums[i+1:].index(needed) + (i + 1)]
