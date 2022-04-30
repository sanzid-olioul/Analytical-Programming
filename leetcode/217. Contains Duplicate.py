class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dc = dict()
        for i in range(len(nums)):
            dc[nums[i]] = dc.get(nums[i],0) + 1
            if dc[nums[i]] >1 :
                return True
        return False