class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in nums: 
            mod=i%3
            if mod==2:
                count+=1
            else:
                count+=mod
        return count