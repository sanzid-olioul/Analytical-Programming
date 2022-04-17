class Solution:
    def triangularSum(self, nums) -> int:
        temp = []
        ln = len(nums)
        for i in range(1,ln):
            for j in range(ln-i):
                nm = (nums[j] + nums[j+1])%10
                temp.append(nm)
            nums = temp
            temp = []
            
        return nums[0]
