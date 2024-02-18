class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        ldiags = set()
        rdiags = set()
        cols = set()
        def fn(idx,rows):
            if idx == n:
                res.append(["".join(row) for row in rows])
                return   
            for i in range(n):
                ldiag = i+idx
                rdiag = i-idx
                col = i
                if col not in cols and ldiag not in ldiags and rdiag not in rdiags:
                    cols.add(col)
                    ldiags.add(ldiag)
                    rdiags.add(rdiag)
                    row = ["."]*n
                    row[col] = "Q"
                    rows.append(row)
                    fn(idx+1,rows)
                    rows.pop()
                    rdiags.remove(rdiag)
                    ldiags.remove(ldiag)
                    cols.remove(col)
                              
        fn(0,[])
        return res

            
        