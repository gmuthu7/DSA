class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        if len(strs) == 1 and len(strs[0]) == 0:
            return [[""]]
        for s in strs:
            h = "".join(sorted(s))
            if h not in d:
                d[h] = []
            d[h].append(s)
        return [d[t] for t in d]
            

        
        