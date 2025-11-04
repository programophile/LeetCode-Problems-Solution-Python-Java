class Solution(object):
    def findXSum(self, nums, k, x):
        i = 0
        list2 = []
        while i < len(nums)-k+1:
            dict1 = {}
            for j in nums[i:i+k]:
                if j in dict1:
                    dict1[j] += 1
                else:
                    dict1[j] = 1
            sorted_items = sorted(dict1.items(), key=lambda item: (-item[1], -item[0]))
            total = 0
            for key, value in sorted_items[:x]:
                total += key * value
            list2.append(total)
            i += 1
        return list2
