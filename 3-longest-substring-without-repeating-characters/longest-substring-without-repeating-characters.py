class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        longest = 0
        m = set()
        while j < len(s):
            if s[j] not in m:
                m.add(s[j])
                j+=1
                if longest < (j-i):
                    longest = j - i
            else:
                while s[i] != s[j]:
                    m.remove(s[i])
                    i+=1
                i+=1
                j+=1
        return longest
            
        