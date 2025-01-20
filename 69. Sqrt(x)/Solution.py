class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        a = x // 2
        while a * a > x:
            a = (a + (x // a)) // 2
        return a

        
        
        