"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # typical sliding window problem
        profit = 0
        l = 0
        for r in range(len(prices)):
            # if left price is greater than right, shift one over
            if prices[l] > prices[r]:
                l = r
            else:
                # get profit from sliding window and compare with last profit
                profit = max(profit, prices[r] - prices[l])
        return profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
