class Solution(object):
    def majorityElement(self, nums):
        dict={}
        for i in nums:
            if i not in dict.keys():
                dict[i]=1
            else:
                dict[i]+=1
        pair=[0,0]
        for key,value in dict.items():
            if value>pair[1]:
                pair[0]=key
                pair[1]=value
        return pair[0]

        
        