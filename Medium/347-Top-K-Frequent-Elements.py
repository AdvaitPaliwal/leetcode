"""
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = dict()
        for i in set(nums):
            d[i] = nums.count(i)
        sorted_d = {k: v for k, v in sorted(
            d.items(), key=lambda item: item[1], reverse=True)}
        return list(sorted_d.keys())[:k]


nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
