class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # tmp variable to save previous value,
        # where do we get the first house from once we're at the 3rd?
        tmp = 0
        # set the current amount to the first house as a given
        amount = nums[0]
        # skip first since already assigned
        for num in nums[1:]:
            # max(current house + last house, existing max sum)
            max_sum = max(num+tmp, amount)
            # reassign amount to save somewhere
            tmp = amount
            # current max sum that's been computed
            amount = max_sum

        # finally reached end, return amount
        return amount


nums = [2, 1, 1, 2]
print(Solution().rob(nums))
