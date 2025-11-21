class Solution(object):
    def countPalindromicSubsequence(self, s):
        first = {}
        last = {}

       
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        result = 0

       
        for ch in first:
            if last[ch] - first[ch] > 1: 
                middle = set(s[first[ch] + 1 : last[ch]])
                result += len(middle)

        return result

        
