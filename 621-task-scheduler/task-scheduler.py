class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = defaultdict(int)
        pos = defaultdict(lambda: -1)
        tot = len(tasks)
        i = 0
        for task in tasks:
            d[task] += 1
        while tot > 0:
            chosen = None
            least_pos = float("inf")
            for key in d:
                if d[key]>0:
                    if (pos[key] == -1 or i - pos[key] > n) and (not chosen or d[chosen] < d[key]):
                            chosen = key
                    least_pos = min(least_pos,pos[key])
            if chosen:
                d[chosen]-=1
                pos[chosen]=i
                tot-=1
                i+=1
            else:
                i+= n + least_pos - i + 1
        return i
                

                
            


        
        


        

        