class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = set(nums[i])

        res = nums[0]
        for i in range(1,len(nums)):
            res = res.intersection(nums[i])

        return sorted(list(res))