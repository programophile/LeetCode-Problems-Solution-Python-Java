# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_pointer=head
        fast_pointer=head
        while fast_pointer:
            try:
                slow_pointer=slow_pointer.next
                fast_pointer=fast_pointer.next.next
                if slow_pointer==fast_pointer:
                    return True
            except:
                return False
        return False
        