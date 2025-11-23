class Solution(object):
    def maxSumDivThree(self, nums):
        total = 0
        smallest_one = float('inf')
        smallest_two = float('inf')

        for x in nums:
            total += x

            r = x % 3

            if r == 1:
               
                smallest_two = min(smallest_two, smallest_one + x)
                smallest_one = min(smallest_one, x)

            elif r == 2:
                smallest_one = min(smallest_one, smallest_two + x)
                smallest_two = min(smallest_two, x)

       
        if total % 3 == 0:
            return total

       
        if total % 3 == 1:
            return total - smallest_one

       
        return total - smallest_two
