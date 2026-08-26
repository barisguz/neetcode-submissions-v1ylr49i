class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ## matrix [[1,0,5],[2,4,3]]
        ##
##.         [1,0,5]
##          [2,4,3]
        ##
        ## matrix2[[2,-1],[1,3]]
        ## matrixResult[[2,1],[-1,3]]
        ##

        rows = len(matrix)
        cols = len(matrix[0])

        newMatrix = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                newMatrix[c][r] = matrix[r][c]

        return newMatrix