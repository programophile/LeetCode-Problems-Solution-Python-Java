class Solution(object):
    def findWordsContaining(self, words, x):
        new_arr=[]
        for i in range(len(words)):
            if x in words[i]:
                new_arr.append(i)
        return new_arr