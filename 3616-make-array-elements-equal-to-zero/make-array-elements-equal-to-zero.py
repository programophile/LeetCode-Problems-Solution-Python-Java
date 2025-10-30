class Solution(object):
    def countValidSelections(self, nums):
        count=0
        for i in range (len(nums)):
            if nums[i]==0:
                if sum(nums[:i])==sum(nums[i:]):
                    count+=2
                elif sum(nums[:i])-sum(nums[i:])==1 or sum(nums[:i])-sum(nums[i:]) == -1:
                    count+=1
        return count