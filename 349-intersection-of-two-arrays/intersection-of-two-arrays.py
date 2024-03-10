class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        s2 = set(nums2)
        for num in list(s1):
            if num not in s2 :
                s1.remove(num)
        return list(s1)
        
        