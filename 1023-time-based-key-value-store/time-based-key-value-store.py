class TimeMap(object):

    def __init__(self):
        self.d = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.d[key] = self.d.get(key,[]) + [(value,timestamp)]
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        lst = self.d.get(key,[])
        left = 0
        right = len(lst) - 1
        while left <= right:
            mid = (left + right)//2
            if lst[mid][1] <= timestamp and (mid + 1 == len(lst) or lst[mid+1][1]>timestamp):
                return lst[mid][0]
            elif lst[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        return ""


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)