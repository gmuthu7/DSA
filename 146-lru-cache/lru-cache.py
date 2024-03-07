class TreeNode:
    def __init__(self,k,v,p,n):
        self.val = v
        self.key = k
        self.next = n
        self.prev = p

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = {}
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.num = 0

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        if self.num >=2:
            node = self.d[key]
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        return self.d[key].val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.get(key) != -1:
            self.d[key].val = value
            return
        node = TreeNode(key,value,None,self.head)
        self.head = node
        self.d[key] = node
        if node.next:
            node.next.prev = node
        self.num+=1
        if self.num == 1:
            self.tail = node
        if self.num > self.capacity:
            self.num-=1
            temp = self.tail.prev
            del self.d[self.tail.key]
            del self.tail
            self.tail = temp
            self.tail.next = None
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)