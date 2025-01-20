import math
class Solution(object):
    def maxAdjacentDistance(self, nums):
        max_diff=nums[0]-nums[1]
        for i in range(len(nums)-1):
            max_diff=max(max_diff,abs(nums[i]-nums[i+1]))
        max_diff=max(max_diff,abs(nums[0]-nums[-1]))
        return max_diff