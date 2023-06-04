"""
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # basic binary search
        low, high = 0, len(nums) - 1
        while low <= high:
            # to prevent overflow
            mid = low + ((high - low) // 2)
            # if current mid is greater than target
            if nums[mid] > target:
                # move current high down 1
                high = mid - 1
            # if current mid is less than target
            elif nums[mid] < target:
                # move current low up 1
                low = mid + 1
            # if current mid is equal to target
            else:
                # found it
                return mid
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search(nums, target))
