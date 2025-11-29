class Solution(object):
    def minOperations(self, nums, k):
        total=sum(nums)
        reminder=total%k
        return reminder