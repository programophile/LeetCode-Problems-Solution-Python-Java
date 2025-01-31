class Solution(object):
    def singleNumber(self, nums):
        result = 0  # Initialize result to 0
        for num in nums:
            result ^= num  # XOR each number with the result
        return result  # Return the single number
