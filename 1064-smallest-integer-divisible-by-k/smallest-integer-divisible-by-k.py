class Solution(object):
    
    def smallestRepunitDivByK(self, k):
        current=1
        count=1
        prev=set()
        if k%2==0 or k%5==0:
            return -1
        while current%k:
            if current in prev:
                return -1
            prev.add(current)
            current=10*(current%k)+1
            count+=1
        return count
        