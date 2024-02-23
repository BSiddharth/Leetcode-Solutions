# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
# git add . && git commit -m "completed longest_increasing_path_in_a_matrix" && git push && exit

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        matrix_mem = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        result = 0

        def helper(row,col):
            if matrix_mem[row][col] != None:
                return matrix_mem[row][col]

            next_tile = [
                 (row + 1,col),
                 (row,col + 1),
                 (row - 1,col),
                 (row,col - 1),
             ]
            helper_result = 1

            for nt in next_tile:
                if  0 <= nt[0] < len(matrix) and 0 <= nt[1] < len(matrix[0]) and matrix[nt[0]][nt[1]] > matrix[row][col]:
                    sub_result = 1 + helper(nt[0],nt[1])
                    if sub_result > helper_result:
                        helper_result = sub_result

            matrix_mem[row][col] = helper_result

            return helper_result

                    


        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                helper_result = helper(row,col)

                if helper_result > result:
                    result = helper_result

        return result
