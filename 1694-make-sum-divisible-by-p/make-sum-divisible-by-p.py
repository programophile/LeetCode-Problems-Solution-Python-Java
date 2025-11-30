class Solution(object):
    def minSubarray(self, nums, p):
        prefix_sum=[nums[0]]
        for i in range(1,len(nums)):
            prefix_sum.append(prefix_sum[i-1]+nums[i])
        remainder=sum(nums)%p
        if remainder==0:
            return 0
        seen = {0: -1}
        best = len(nums)

        for i in range(len(nums)):
            curr = prefix_sum[i] % p
            target = (curr - remainder) % p

            if target in seen:
                best = min(best, i - seen[target])

            seen[curr] = i

        return best if best < len(nums) else -1
        



