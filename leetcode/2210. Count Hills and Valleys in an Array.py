class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hill = 0
        vally = 0
        for i in range(1,len(nums)-1):
            if nums[i]<nums[i+1] and nums[i]< nums[i-1]:
                vally+=1
            if nums[i]>nums[i+1] and nums[i]> nums[i-1]:
                hill+=1
        
        return max(hill,vally)