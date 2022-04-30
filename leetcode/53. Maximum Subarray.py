class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi, curr = nums[0] , 0
        for i in range(len(nums)):
            curr += nums[i]
            maxi = max(maxi, curr)
            if curr <= 0:
                curr = 0
        return maxi