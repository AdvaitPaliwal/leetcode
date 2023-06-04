"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # assign previous to one before head and current to head so we can swap
        prev, curr = None, head
        while curr:
            # swap previous and current using a temporary variable
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # prev is at the head of the reversed linked list
        return prev
