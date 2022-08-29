'''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #initiates empty dictionary
        d = dict()
        #iterates through counter and nums pairs
        for i,n in enumerate(nums):
            #searches for sum pair
            match = target - n
            #returns indices if pair is found
            if match in d:
                return d[match], i
            #adds pair to d
            else:
                d[n] = i

nums = [2,7,11,15]
target = 26
print(Solution().twoSum(nums, target))