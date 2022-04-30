class Solution:
    def search(self, nums: List[int], target: int) -> int:
        fs = 0
        ls = len(nums)-1
        while fs <= ls:
            md = (fs + ls )//2
            if nums[md] == target:
                return md
            elif nums[md] > target:
                ls = md-1
            else:
                fs = md+1
        return -1