import math

class Solution(object):
    def generate(self, numRows):
        arr1 = []
        for i in range(numRows):  
            arr = []
            for j in range(i + 1):  
                arr.append(math.factorial(i) // (math.factorial(j) * math.factorial(i - j)))
            arr1.append(arr)
        return arr1



