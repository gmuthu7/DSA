class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left<=right:
            mid = (left + right)//2
            m = nums[mid]
            l = nums[left]
            r = nums[right]
            if m == target:
                return mid
            if left == right:
                return -1
            elif l <= m <= r:
                if target < m:
                    right = mid - 1
                else:
                    left = mid + 1
            elif l <= m:
                if l <= target <= m:
                    right = mid - 1
                else:
                    left = mid + 1
            elif m <= r:
                if m <= target <= r:
                    left = mid + 1
                else:
                    right = mid - 1
        return - 1