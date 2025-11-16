class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        M = 1000000007
        total_num=0
        count=0
        for i in range(0,len(s)):
            if  s[i]=="1":
                count+=1
            else:
                
                count=0
            total_num=(total_num+count)%M
        return total_num


        