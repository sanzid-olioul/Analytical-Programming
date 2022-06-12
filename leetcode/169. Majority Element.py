class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = Counter(nums)
        res = None

        for k in val.keys():
            if res == None:
                res =k
            elif val[res] < val[k]:
                res = k
        print(val)
        return res

        
        