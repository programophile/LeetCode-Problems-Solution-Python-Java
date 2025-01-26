class Solution(object):
    def letterCombinations(self, digits):
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result=[]
        if len(digits)==0:
            return []
        self.dfs(digits,0,dic,"",result)
        return result
    def dfs(self,nums,index,dic,path,result):
        if index>=len(nums):
            result.append(path)
            return
        str1=dic[nums[index]]
        for i in str1:
            self.dfs(nums,index+1,dic,path+i,result)

        
        