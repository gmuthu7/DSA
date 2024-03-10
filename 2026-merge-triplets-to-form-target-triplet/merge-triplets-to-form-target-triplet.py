class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        def isValidTriplet(triplet,target):
            if triplet[0] == target[0] and triplet[1] == target[1] and triplet[2] == target[2]:
                return 2
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                return 1
            return 0
        curr = [0,0,0]
        for idx,triplet in enumerate(triplets):
            if isValidTriplet(triplet,target):
                curr = [max(curr[0],triplet[0]),max(curr[1],triplet[1]),max(curr[2],triplet[2])]
                if isValidTriplet(curr,target) == 2:
                    return True
        return False
            
        