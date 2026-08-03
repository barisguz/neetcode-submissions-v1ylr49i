class Solution:
    def isPathCrossing(self, path: str) -> bool:
        been = []
        x,y = 0, 0
        coordinates = (x,y)
        been.append(coordinates)
        for i in path: 
            if (i == 'N'):
                y += 1
            elif(i == 'S'):
                y -= 1
            elif(i == 'E'):
                x += 1
            elif(i == 'W'): 
                x -= 1
            coordinates = (x,y)
            if(coordinates in been):
                return True
            been.append(coordinates)
        return False
        