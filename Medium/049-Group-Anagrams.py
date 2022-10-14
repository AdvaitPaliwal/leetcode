"""
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = dict()
        for s in strs:
            # sort every word and append to hashMap values
            sorted_s = ''.join(sorted(s))
            if sorted_s in hashMap:
                hashMap[sorted_s] += [s]
            else:
                hashMap[sorted_s] = [s]
        return list(hashMap.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
