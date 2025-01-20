class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            for i in range(0,len(haystack)):
                if str(haystack[i:len(needle)+i])==needle:
                    return i
        return -1

