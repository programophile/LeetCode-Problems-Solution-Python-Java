# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        nums = set(nums)  
        while head and head.val in nums:
            head = head.next
        prev = head
        if not prev:
            return None
        current = head.next

        while current:
            if current.val in nums:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next

        return head
