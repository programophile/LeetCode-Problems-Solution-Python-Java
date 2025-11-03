class Solution(object):
    def minCost(self, colors, neededTime):
        total=0
        # i=0
        # j=1
        for i in range(1,len(colors)):
            if colors[i]==colors[i-1]:
                total+=min(neededTime[i],neededTime[i-1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
                # neededTime
        return total
        # while j<len(colors):
        #     if colors[i]==colors[j]:
        #         arr.append(neededTime[i],needed)
        