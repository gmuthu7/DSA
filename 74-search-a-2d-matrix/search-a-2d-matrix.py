class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        def fn(idx):
            row_idx = idx// n
            col_idx = idx % n
            return matrix[row_idx][col_idx]
        left = 0
        right = (m*n) -1
        while left<=right:
            mid = (right+left) // 2
            el = fn(mid)
            if el == target:
                return True
            elif el < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

        