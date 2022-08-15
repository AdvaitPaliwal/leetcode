'''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
'''
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i,n in enumerate(nums):
            match = target - n
            if match in d:
                return d[match], i
            else:
                d[n] = i

nums = [2,7,11,15]
target = 26
print(Solution().twoSum(nums, target))