
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        return findMedianSortedArrays(nums1,nums2)
    def findMedianSortedArrays(self, nums1, nums2):
        arr = nums1 + nums2
        arr.sort()
        n = len(arr)

        mid = n // 2

        if n % 2 == 1:
            return float(arr[mid])
        else:
            return (arr[mid - 1] + arr[mid]) / 2.0