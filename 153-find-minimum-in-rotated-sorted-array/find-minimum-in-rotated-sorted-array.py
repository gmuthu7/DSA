class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        5,6,7,8,9,0,1,2,3,4
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right+left)//2
            forward = (mid+1)%len(nums)
            backward = mid-1
            if nums[mid] <= nums[backward] and nums[mid] <= nums[forward]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid +1
            else:
                right = mid - 1
        
        