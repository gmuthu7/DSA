class Solution(object):
    def check_sub_sudoku(self,board,i,j):
        s = set()
        for i_ in range(i,i+3):
            for j_ in range(j,j+3):
                val = board[i_][j_]
                if val != ".":
                    if val in s:
                        return False
                    s.add(val)
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                val1 = board[i][j]
                val2 = board[j][i]
                if i%3 == 0 and j%3 == 0:
                    if not self.check_sub_sudoku(board,i,j):
                        return False
                if val1 != ".":
                    if val1 in row_set:
                        return False
                    row_set.add(val1)
                if val2 != ".":
                    if val2 in col_set:
                        return False
                    col_set.add(val2)
        return True