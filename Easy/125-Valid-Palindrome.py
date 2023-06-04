"""
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # reverse s without punctuation and all lowercase
        new_s = "".join(i for i in s if i.isalnum()).lower()[::-1]
        # check if new s == reversed new s
        return new_s == new_s[::-1]


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
