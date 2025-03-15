class Solution(object):
    def isMatch(self, s, p):
        i, j = 0, 0
        star, match = -1, 0  # Star position & match position
        
        while i < len(s):
            if j < len(p) and (p[j] == '?' or p[j] == s[i]):  
                # Characters match or '?' wildcard
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':  
                # '*' wildcard: store its position & match index in s
                star = j
                match = i
                j += 1
            elif star != -1:  
                # Last seen '*' allows us to adjust match
                j = star + 1
                match += 1
                i = match
            else:
                return False  # No match possible
        
        # Remaining characters in p must be all '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)


