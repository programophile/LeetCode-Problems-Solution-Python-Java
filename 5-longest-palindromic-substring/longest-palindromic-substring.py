class Solution(object):
    def longestPalindrome(self, s):
        start,end=0,0
        if len(s)<1:
            return ""
        def pali_check(l,r):
            l=int(l)
            r=int(r)
            while l>=0 and r<len(s) and s[l]==s[r]:
                l=l-1
                r=r+1
            return r-l-1
        for i in range(len(s)):
            len1=pali_check(i,i)
            len2=pali_check(i,i+1)
            max_len=max(len1,len2)
            if max_len>end-start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end+1]
