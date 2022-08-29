'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        #set creates a collection of unique elements
        for c in set(s):
            #if the number of occurances of characters in set(s) are not equal, return false
            if s.count(c) != t.count(c):
                return False
        return True

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))