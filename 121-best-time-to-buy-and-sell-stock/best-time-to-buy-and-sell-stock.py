class Solution(object):
    def maxProfit(self, prices):
        left,right=0,0
        profit=0
        while right<len(prices):
            
            if prices[left]>=prices[right]:
                left=right
                right+=1
            else:
                profit=max(profit,prices[right]-prices[left])
                right+=1

            
        return profit