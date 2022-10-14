"""
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The XOR of any two identical numbers is 0. For example, 0101 ^ 0101 = 0000.
        # The XOR of any number and 0 is the number itself. For example, 0101 ^ 0000 = 0101
        res = 0
        for n in nums:
            res ^= n
        return res


nums = [4, 1, 2, 1, 2]
print(Solution().singleNumber(nums))
