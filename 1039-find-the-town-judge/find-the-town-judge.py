class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        d = {}
        if not trust:
            if n == 1:
                return 1
            else:
                return -1
        judge_label = -1
        for t in trust:
            d[t[0]] = -1
            if judge_label == t[0]:
                judge_label = -1
            d[t[1]] = d.get(t[1],0)+1
            if d[t[1]] == 0:
                d[t[1]] = -1
            if d[t[1]] == n - 1:
                if judge_label != -1:
                    return -1
                judge_label = t[1]
        return judge_label
            
        