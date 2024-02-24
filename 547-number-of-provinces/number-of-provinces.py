class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        1 2 3 4 5
        """
        num_provinces = n = len(isConnected)
        rank = [1]*num_provinces
        parent = range(num_provinces)
        def find(idx):
            if parent[idx] == idx:
                return idx
            parent[idx] = find(parent[idx])
            return parent[idx]
        def union(i1,i2):
            p1 = find(i1)
            p2 = find(i2)
            if p1 == p2:
                return False
            rank1 = rank[p1]
            rank2 = rank[p2]
            if rank1 == rank2:
                parent[p2] = p1
                rank[p1] += 1
            elif rank1 < rank2:
                parent[p1] = p2
            elif rank1 > rank2:
                parent[p2] = p1
            return True
        for i in range(n):
            for j in range(i,n):
                if i != j and isConnected[i][j] == 1:
                    if union(i,j):
                        num_provinces-=1
        return num_provinces

