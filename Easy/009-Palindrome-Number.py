"""
    Given an integer x, return true if x is palindrome integer.

    An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #negative number returns False
        if x < 0:
            return False
        #converts to string, reverses, and compares with original
        else:
            return str(x)[::-1] == str(x)

x = 121
print(Solution().isPalindrome(x))