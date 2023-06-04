"""
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # iterate over every unique char in ransom note
        # compare occurance of each char in each
        # num of char in ransomNote should be <= num of char in magazine count
        # use all function to get bool value
        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))


ransomNote = "abc"
magazine = "cbdea"
print(Solution().canConstruct(ransomNote, magazine))
