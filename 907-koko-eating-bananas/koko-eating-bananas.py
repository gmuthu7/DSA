class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def check(k):
            if k == 0:
                return False
            _h = h
            for pile in piles:
                mod = pile % k
                div = pile // k
                if not mod:
                    _h-=div
                else:
                    _h-=div+1
                if _h < 0:
                    return False
            return True

        right = max(piles)
        left = 1
        while left <= right:
            mid = (left + right)//2
            flag_mid = check(mid)
            if flag_mid:
                if not check(mid-1):
                    return mid
                else:
                    right = mid - 1
            else:
                if check(mid+1):
                    return mid+1
                else:
                    left = mid + 1

                

        
        