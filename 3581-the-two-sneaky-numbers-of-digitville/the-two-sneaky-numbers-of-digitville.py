class Solution(object):
    def getSneakyNumbers(self, nums):
        new_arr=[]
        output_list=[]
        for i in nums:
            if i in new_arr:
                    output_list.append(i)
            else :
                new_arr.append(i)
        return output_list