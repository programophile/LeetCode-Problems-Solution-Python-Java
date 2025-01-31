class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        while temp and temp.next:  # Ensure temp.next is not None
            if temp.val == temp.next.val:
                temp.next = temp.next.next  # Skip the duplicate node
            else:
                temp = temp.next  # Move to the next node
        return head  # Return the modified list
