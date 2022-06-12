class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dct = {0:0,1:0,2:0}
        for dt in nums:
            dct[dt]+=1
        
        res = [0]*dct[0] + [1]*dct[1] +[2]*dct[2]
        for i in range(len(nums)):
            nums[i]= res[i]