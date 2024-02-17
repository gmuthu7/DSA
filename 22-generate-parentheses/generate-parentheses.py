class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left = right = n
        res = []
        def fn(left,right,res,curr=""):
            if left == n and right == n:
                res.append(curr)
                return
            extra_left = left - right
            if extra_left == 0:
                if left < n:
                    fn(left+1,right,res,curr + "(")
            else:
                if left < n:
                    fn(left+1,right,res,curr + "(")
                if right < n:
                    fn(left,right+1,res,curr + ")")
            return res
        return fn(0,0,res)

        