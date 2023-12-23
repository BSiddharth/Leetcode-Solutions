# https://leetcode.com/problems/word-search/description/
# git add . && git commit -m "completed word_search" && git push && exit


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i, j, ind, visited):
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0:
                return False
            if (i, j) in visited:
                return False
            visited.add((i, j))
            char_at_pos = board[i][j]

            if char_at_pos != word[ind]:
                return False
            else:
                if ind == len(word) - 1:
                    return True

            moves_list = [
                (i, j + 1),
                (i + 1, j),
                (i, j - 1),
                (i - 1, j),
            ]

            for move in moves_list:
                if helper(move[0], move[1], ind + 1, visited.copy()):
                    return True
            return False

        # saves a lot of time to check if its possible for the board to contain the word.
        boardDic = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardDic[board[i][j]] += 1

        wordDic = Counter(word)
        for c in wordDic:
            if c not in boardDic or boardDic[c] < wordDic[c]:
                return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, 0, set()):
                    return True

        return False
