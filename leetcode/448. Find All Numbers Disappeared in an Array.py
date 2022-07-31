class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ano = [0 for i in range(len(nums))]
        rem = []
        for n in nums:
            ano[n-1]+=1
        for i in range(len(nums)):
            if ano[i]==0:
                rem.append(i+1)
        return rem
        

