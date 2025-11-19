class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        final_nums=original
        while True:
            if final_nums in nums:
                final_nums*=2
            else:
                return final_nums
        return final_nums