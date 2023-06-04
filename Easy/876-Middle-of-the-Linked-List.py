"""
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # initalize separate instances of slow and fast linked lists
        slow = fast = head
        # while fast is not at the end
        while fast and fast.next:
            # move slow one ahead
            slow = slow.next
            # move fast two ahead
            fast = fast.next.next
        # when fast reaches the end, slow is at the middle
        return slow
