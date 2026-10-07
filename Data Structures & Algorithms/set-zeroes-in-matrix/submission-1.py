class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        r = set()
        c = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        
        for row in r:
            for j in range(cols):
                matrix[row][j] = 0
                
        for col in c:
            for i in range(rows):
                matrix[i][col] = 0