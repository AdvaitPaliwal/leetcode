class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = []
        i = 0
        p = ""
        while i < len(s) - 1:
            p+=s[i]
            if s[i] not in p:
                i+=1
                output.append(p)
                p = ""

        return len(output)


s = "abacaba"
print(Solution().partitionString(s))