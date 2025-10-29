class Solution(object):
    def smallestNumber(self, n):
        while True:
            binary_str = bin(n)[2:]  
            if all(ch == '1' for ch in binary_str):  
                return n
            n += 1
