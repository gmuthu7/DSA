class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens = sorted(tokens)
        left = 0
        right = len(tokens) - 1
        score = 0
        max_score = 0
        while left <= right:
            tl = tokens[left]
            tr = tokens[right]
            if power - tl >= 0:
                power = power - tl
                score+=1
                max_score = max(score,max_score)
                left+=1
            elif score >= 1:
                power = power + tr
                score-=1
                right-=1
            else:
                return score
        return max_score

        