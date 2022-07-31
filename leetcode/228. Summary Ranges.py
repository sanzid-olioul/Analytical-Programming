class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return 
        i = 0 
        n = len(nums)-1
        res = ""
        lst1 = []
        while i < n:
            if nums[i+1] == nums[i]+1:
                if res == "":
                    res = res + str(nums[i])
                    i += 1 
                else:
                    i += 1 
            else:
                if res != "":
                    res += "->"+str(nums[i])
                else:
                    res += str(nums[i])
                lst1.append(res)
                res = ""
                i += 1
        if res == "":
            lst1.append(str(nums[n]))
        else:
            res += "->"+str(nums[n])
            lst1.append(res)
        return lst1