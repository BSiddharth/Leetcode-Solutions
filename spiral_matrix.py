# https://leetcode.com/problems/spiral-matrix/description/
# git add . && git commit -m "completed spiral_matrix" && git push && exit

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = -1
        bottom = len(matrix)
        left = -1
        right = len(matrix[0])
        result  = []
        current_pos = [0,0]
        count = 0
        while (top + 1< bottom):
            while current_pos[1] < right:
                result.append(matrix[current_pos[0]][current_pos[1]])
                
                current_pos[1] += 1
            top += 1
            current_pos[0] += 1
            current_pos[1] -= 1


            while current_pos[0] < bottom:
                result.append(matrix[current_pos[0]][current_pos[1]])
                
                current_pos[0] += 1
            right -= 1
            current_pos[0] -= 1
            current_pos[1] -= 1
                
            while current_pos[1] > left:
                result.append(matrix[current_pos[0]][current_pos[1]])
                
                current_pos[1] -= 1
            bottom -= 1
            current_pos[0] -= 1
            current_pos[1] += 1

            while current_pos[0] > top:
                result.append(matrix[current_pos[0]][current_pos[1]])
                
                current_pos[0] -= 1
            left += 1
            current_pos[0] += 1
            current_pos[1] += 1
            
        return result[:len(matrix)*len(matrix[0])]
