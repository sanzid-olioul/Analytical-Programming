class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return list(sorted(nums))[-k]