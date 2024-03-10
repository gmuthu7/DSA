class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        3 -> 4 -> 2 -> 3 -> 4 -> 2 -> 3
        
        1 -> 3 -> 2 -> 4 -> 2 -> 4
        """
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        cycle_length = 0
        ptr = slow
        while True:
            ptr = nums[ptr]
            cycle_length+=1
            if ptr == slow:
                break
        fast = nums[0]
        while cycle_length != 0:
            fast = nums[fast]
            cycle_length-=1
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        