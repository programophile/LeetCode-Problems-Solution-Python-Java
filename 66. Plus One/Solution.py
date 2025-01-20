class Solution(object):
    def plusOne(self, digits):
        num = 0
        # Convert the digits array to a single integer
        for digit in digits:
            num = num * 10 + digit  # Account for place values

        # Add 1 to the number
        num += 1

        # Convert the resulting number back to a list of digits
        return [int(d) for d in str(num)]
