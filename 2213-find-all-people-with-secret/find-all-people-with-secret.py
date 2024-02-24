class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        rank = [1]*n
        rep = range(n)
        s = set([0,firstPerson])
        def find(idx):
            if rep[idx] == idx:
                return idx
            else:
                rep[idx] = find(rep[idx])
                return rep[idx]
        
        def union(i1,i2):
            r1 = find(i1)
            r2 = find(i2)
            if r1 == r2:
                return
            rank1 = rank[r1]
            rank2 = rank[r2]
            if rank1 > rank2:
                rep[r2] = r1
            elif rank2 > rank1:
                rep[r1] = r2
            else:
                rep[r2] = r1
                rank[r1]+=1 
        union(0,firstPerson) 
        meetings = sorted(meetings,key=lambda x:x[2])
        prev_idx = 0
        for idx in range(len(meetings)+1):
            meeting = None if idx == len(meetings) else meetings[idx]
            if not meeting or meetings[prev_idx][2] != meeting[2]:
                p0 = find(0)
                while prev_idx < idx: 
                    sub_meeting = meetings[prev_idx]
                    p1 = find(sub_meeting[0])
                    p2 = find(sub_meeting[1])
                    if p1 != p0 and p2 != p0:
                        rep[sub_meeting[0]] = sub_meeting[0]
                        rep[sub_meeting[1]] = sub_meeting[1]
                        rank[sub_meeting[0]] = 1
                        rank[sub_meeting[1]] = 1
                    else:
                        s.add(sub_meeting[0])
                        s.add(sub_meeting[1])
                    prev_idx+=1
            if meeting:
                union(meeting[0],meeting[1])
        return list(s)

        