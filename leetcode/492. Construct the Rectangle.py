import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        vl = math.floor(math.sqrt(area))
        for i in range(vl,0,-1):
            if area %i ==0:
                return [area//i,i]
