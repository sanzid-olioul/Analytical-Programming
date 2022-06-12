class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        for k,v in c1.items():
            c2[k] = c2.get(k,0)
            res += [k]*min(c1[k],c2[k])
        return res

