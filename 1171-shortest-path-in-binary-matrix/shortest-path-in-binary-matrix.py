class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(1,1),(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
        n = len(grid)
        queue = collections.deque()
        queue.append((0,0))
        visited = set()
        level = 0
        while queue:
            level+=1
            for _ in range(len(queue)):
                row,col = queue.popleft()
                if  grid[row][col] == 1 or (row,col) in visited:
                    continue
                if row == n-1 and col == n-1:
                    return level
                visited.add((row,col))
                for direction in directions:
                    nrow = row+direction[0]
                    ncol = col+direction[1]
                    if nrow <0 or nrow>=n or ncol<0 or ncol>=n:
                        continue
                    queue.append((nrow,ncol))
        return -1



