class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        cou = 0
        i = 0
        while i < len(nums)-1:
            if i <0:
                i=0
            elif len(nums)> i and nums[i] == nums[i+1]:
                nums.pop(i)
                i-=2
                cou+=1
            else:
                i+=2
        if len(nums) %2 ==1:
            cou+=1
        return cou