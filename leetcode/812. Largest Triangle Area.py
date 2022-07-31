class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        from itertools import combinations
        area=[]
        for x in list(combinations(points,3)):
            a= (abs(x[1][1]-x[0][1])**2 + abs(x[1][0]-x[0][0])**2)**0.5
            b = (abs(x[2][1] - x[0][1]) ** 2 + abs(x[2][0] - x[0][0]) ** 2) ** 0.5
            c = (abs(x[2][1] - x[1][1]) ** 2 + abs(x[2][0] - x[1][0]) ** 2) ** 0.5
            s= (a+b+c)/2
            t= ((s-a)*(s-b)*(s-c)*s)**0.5
            area.append(round(t,2))
        return (max(area))
        