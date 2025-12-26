class Solution(object):
    def searchRange(self, nums, target):
        def findLeft():
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    res = mid
            return res

        def findRight():
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    res = mid
            return res

        return [findLeft(), findRight()]
