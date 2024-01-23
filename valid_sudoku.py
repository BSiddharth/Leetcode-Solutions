# https://leetcode.com/problems/valid-sudoku/description/
# git add . && git commit -m "completed valid_sudoku" && git push && exit

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_list = [[] for _ in range(9)]
        col_list = [[] for _ in range(9)]
        sub_box_list = [[[] for _ in range(3)] for _ in range(3)]

        for x in range(len(board)):
            for y in range(len(board)):
                current_num = board[x][y]
                if current_num == ".":
                    continue
                if current_num in row_list[x]:
                    return False
                if current_num in col_list[y]:
                    return False
                
                x_index = x//3 
                y_index = y//3

                if current_num in sub_box_list[x_index][y_index]:
                    return False
                row_list[x].append(current_num)
                col_list[y].append(current_num)
                sub_box_list[x_index][y_index].append(current_num)

        return True
