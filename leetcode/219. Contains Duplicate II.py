class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        uniqueDict = dict()
        for idx,i in enumerate(nums):
            if i not in uniqueDict:
                uniqueDict[i] = idx 
            else:
                diff = abs(idx-uniqueDict[i])
                if diff <= k:
                    return True
                uniqueDict[i] = idx
        return False