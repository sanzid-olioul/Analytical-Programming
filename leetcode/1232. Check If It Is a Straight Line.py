class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[0][1] ==  coordinates[1][1]:
            for i in range(1,len(coordinates)):
                if coordinates[i-1][1] ==  coordinates[i][1]:
                    continue
                return False
            return True
               
        m = (coordinates[0][0] -  coordinates[1][0])/(coordinates[0][1] -  coordinates[1][1])
        for i in range(1,len(coordinates)):
            try:
                if m == (coordinates[i-1][0] -  coordinates[i][0])/(coordinates[i-1][1] -  coordinates[i][1]) :
                    continue
                return False
            except:
                return False
        return True
