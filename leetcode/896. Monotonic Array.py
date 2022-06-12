class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        pos = False
        neg = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                neg = True
            if nums[i] < nums[i+1]:
                pos= True
        if neg and pos:
            return False
        return True