"""
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # simple recursive fibonacci series
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)


n = 38
print(Solution().climbStairs(n))
