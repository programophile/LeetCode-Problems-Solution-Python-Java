class Solution(object):
    def isAcronym(self, words, s):
        str1=''
        for i in words:
            str1+=i[0]
        if str1==s:
            return True
        return False