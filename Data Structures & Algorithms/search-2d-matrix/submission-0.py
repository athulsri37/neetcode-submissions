class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #print(len(matrix), len(matrix[0]))
        rows = len(matrix)
        cols = len(matrix[0])
        f = 0
        l = cols - 1
        targetRow = -1
        for i in range(rows):
            if target>=matrix[i][f] and target<=matrix[i][l]:
                targetRow = i
        for i in range(cols):
            if matrix[targetRow][i] == target:
                return True
        return False