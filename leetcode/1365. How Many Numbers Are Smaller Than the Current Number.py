class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = []
        res = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            lst.append((i,nums[i]))
        lst.sort(key= lambda x:x[1])
        cou = 0
        for i in range(len(nums)):
            if i>0 and lst[i][1]==lst[i-1][1]:
                res[lst[i][0]] = res[lst[i-1][0]]
            else:
                res[lst[i][0]] = cou
            cou+=1
        return res