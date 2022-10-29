"""
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.
"""

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
        # Floyd’s Cycle Finding Algorithm
        # aka tortoise & hare algo
        slow = fast = head
        while fast and fast.next:
            # fast reaches end and cycles
            fast = fast.next.next
            # takes time to catch up
            slow = slow.next
            if slow == fast:
                return True
        return False


head = [1, 2, 4]
print(Solution().hasCycle(head))
