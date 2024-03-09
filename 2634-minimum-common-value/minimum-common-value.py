class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        pos1 = 0
        pos2 = 0
        while pos1 < len(nums1) and pos2 < len(nums2):
            n1 = nums1[pos1]
            n2 = nums2[pos2]
            if n1 == n2:
                return n1
            elif n1 < n2:
                pos1+=1
            else:
                pos2+=1
        return -1
        