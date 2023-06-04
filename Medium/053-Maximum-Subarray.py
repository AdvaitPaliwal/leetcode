"""
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    A subarray is a contiguous part of an array.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's Algorithm
        # sliding window problem
        # need two sums to track current and max sum
        curSum = maxSum = nums[0]
        # since curSum and maxSum are assigned to first index in nums
        # iterate over nums[1:]
        for num in nums[1:]:
            # get the currSum of current window
            curSum = max(num, curSum + num)
            # use currSum to get maxSum
            maxSum = max(maxSum, curSum)

        return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
