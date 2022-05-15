class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        msn = len(nums)
        nums.sort()
        for i in range(msn):
            if nums[i]!=i:
                msn = i
                break
        return msn 