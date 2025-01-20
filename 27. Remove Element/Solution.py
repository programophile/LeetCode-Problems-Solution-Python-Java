class Solution(object):
    def removeElement(self, nums, val):
        count=0
        for i in nums:
            if i==val:
                nums.remove(i),nums.append(i)
               
        return len(nums)-nums.count(val)
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """

#         for i in nums:
#             if i==val:
#                 nums.remove(i), nums.append(i)
#         count=0
#         for i in nums:
#             if i!=val:
#                 count+=1 
#         return count