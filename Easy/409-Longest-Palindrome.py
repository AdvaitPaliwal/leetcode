"""
    Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

    Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_longest_palindrome = 0
        odd_present = False
        # iterate over unique letters in s
        for c in set(s):
            # count the frequency of c in s
            freq = s.count(c)
            # if the count of c in s is even
            if freq % 2 == 0:
                # each c can go on both sides of the palindrome
                len_longest_palindrome += freq
            # else, if the count of c in s is odd,
            else:
                # check bool odd_present to True
                odd_present = True
                # each c - 1 can go on both sides of the palindrome
                # that remaining 1 is mostly useless
                len_longest_palindrome += freq - 1

        if odd_present:
            #  add any one occurance of odd c to the middle
            return len_longest_palindrome + 1
        else:
            # otherwise length is even with each c going on both sides
            len_longest_palindrome


s = "abcdef"
print(Solution().longestPalindrome(s))
