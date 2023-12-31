# https://leetcode.com/problems/set-matrix-zeroes/description/
# git add . && git commit -m "completed set_matrix_zeroes" && git push && exit

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        col_set = set()
        row_set  = set()
        tr = len(matrix)
        tc =len(matrix[0]) 
        for x in range(tr):
            for y in range(tc):
                if not matrix[x][y]:
                    col_set.add(y)
                    row_set.add(x)

        for x in row_set:
            matrix[x] = [0 for _ in range(tc)]
        
        for y in col_set:
            for x in range(tr):
                matrix[x][y] = 0
