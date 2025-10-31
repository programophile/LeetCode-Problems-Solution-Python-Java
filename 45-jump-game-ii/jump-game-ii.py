class Solution:
    def jump(self, nums):
        jumps = 0
        curEnd = 0
        curFarthest = 0
        
        for i in range(len(nums) - 1):
            curFarthest = max(curFarthest, i + nums[i])
            
            if i == curEnd:
                jumps += 1
                curEnd = curFarthest
                
                if curEnd >= len(nums) - 1:
                    break
                    
        return jumps
###Redo it when brain is more clear 