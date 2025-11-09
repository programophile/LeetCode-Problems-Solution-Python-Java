class Solution(object):
    def countOperations(self, num1, num2):
        count=0
        while num1*num2!=0:
            if num1>num2:
                
                count += num1 // num2
                num1 %= num2
            elif num2>num1:
                
                count+=num2//num1
                num2%=num1
            else:
                count+=1
                break
            
        return count
        