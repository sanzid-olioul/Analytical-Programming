class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        def mxind(num):
            mx = 0
            for i in range(len(num)):
                if num[i]> num[mx]:
                    mx = i
            return mx
        def mnind(num):
            mn = 0
            for i in range(len(num)):
                if num[i] < num[mn]:
                    mn = i
            return mn
        
        ln = len(nums)
        mxi = mxind(nums)
        mni = mnind(nums)
        mx = max(mxi,mni)
        mn = min(mxi,mni)
        return min(mn+(ln-mx), mx,ln - mn-1)+1