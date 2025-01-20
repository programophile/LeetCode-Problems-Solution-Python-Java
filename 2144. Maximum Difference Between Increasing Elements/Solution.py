class Solution(object):
    def maximumDifference(self, nums):
        ans=0
        c_min=nums[0]
        for i in nums:
            if i<c_min:
                c_min=i
            ans=max(ans,i-c_min)
        if ans==0:
            return -1
        return ans