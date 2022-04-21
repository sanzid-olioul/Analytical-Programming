class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                mi = min(height[i],height[j])
                if(mx < mi * (j -i)):
                    mx = mi * (j - i)
        return mx