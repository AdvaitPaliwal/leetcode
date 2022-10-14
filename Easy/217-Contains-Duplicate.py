"""
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # uses hashmap -- O(n)
        hashMap = dict()
        for i in nums:
            # return True if number is present in both nums and hashMap
            if i in hashMap:
                return True
            # else add i to hashMap with an arbitrary value
            else:
                hashMap[i] = 1


nums = [1, 2, 3, 1]
print(Solution().containsDuplicate(nums))
