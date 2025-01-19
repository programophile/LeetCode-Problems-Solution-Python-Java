class Solution(object):
    def removeDuplicates(self, nums):
       pointer = 0
       for i in range(1, len(nums)):
            if nums[pointer] != nums[i]:
                pointer += 1
                nums[pointer] = nums[i]
       length = pointer + 1
       return length