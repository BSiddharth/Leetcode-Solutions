# https://leetcode.com/problems/n-queens/description/
# git add . && git commit -m "completed n-queens" && git push && exit

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        
        def helper(row_num,current_chess_board,queens_left,occupied_col,occupied_dig_p,occupied_dig_n):
            for y in range(n):
                if row_num+y in occupied_dig_p:
                    continue
                if row_num-y in occupied_dig_n:
                    continue
                if y in occupied_col:
                    continue
                occupied_col.add(y)
                occupied_dig_p.add(row_num+y)
                occupied_dig_n.add(row_num-y)
                current_chess_board[row_num][y] = 'Q'
                if queens_left == 1:
                    to_append = ["".join(x) for x in current_chess_board]
                    result.append(to_append)
                else:
                    helper(row_num+1,current_chess_board,queens_left-1,occupied_col,occupied_dig_p,occupied_dig_n)
                occupied_col.remove(y)
                occupied_dig_p.remove(row_num+y)
                occupied_dig_n.remove(row_num-y)
                current_chess_board[row_num][y] = '.'
        helper(0,[['.' for _ in range(n)] for _ in range(n)],n,set(),set(),set())
        return result
