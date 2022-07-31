import sys
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dct = {}
        for i in range(len(nums)):
            dct[nums[i]] = dct.get(nums[i],[0,i,i])
            dct[nums[i]][0]+=1
            if dct[nums[i]][1]!=i:
                dct[nums[i]][2] = i
        mx = 0
        diff = sys.maxsize
        for k,v in dct.items():
            if v[0] >mx:
                mx = v[0]
                diff = v[2] - v[1]
            elif v[0]==mx:
                if v[2] - v[1]< diff:
                    diff = v[2] - v[1]
        return diff+1