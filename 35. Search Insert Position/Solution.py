class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Iterate through the list
        for num in range(len(nums)):
            # If target is found, return the index
            if nums[num] == target:
                return num
            # If the current number is greater than the target, return the index
            elif nums[num] > target:
                return num
        
        # If the target is greater than the last element, return the length of the list
        return len(nums)