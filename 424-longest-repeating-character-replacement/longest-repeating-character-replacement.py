class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        AACBC
        AACBBACC
        ACBAAAABA
        l - k > max
        """
        d = defaultdict(int)
        left = 0
        longest = 0
        right = 0
        max_char = None
        while right < len(s):
            c = s[right]
            d[c]+=1
            max_char = c if not max_char or d[max_char] < d[c] else max_char
            l = right - left + 1
            if l - d[max_char] > k:
                d[s[left]]-=1
                left+=1
            else:
                longest = max(longest,l)
            right+=1
        return longest






            
            

        