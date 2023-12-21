# https://leetcode.com/problems/word-search-ii/description/
# git add . && git commit -m "completed word_search_ii" && git push && exit


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def make_trie(words):
            wt = {}

            for word in words:
                current_wt = wt
                for i in range(len(word)):
                    if word[i] not in current_wt:
                        current_wt[word[i]] = {}
                    current_wt = current_wt[word[i]]

                current_wt[None] = None
            return wt

        def delete_from_trie(current_wt, w):
            if w[0] not in current_wt:
                return
            if len(w) == 1:
                if None in current_wt[w]:
                    del current_wt[w][None]
                if len(current_wt[w]) == 0:
                    del current_wt[w]
            else:
                delete_from_trie(current_wt[w[0]], w[1:])
                if len(current_wt[w[0]]) == 0:
                    del current_wt[w[0]]

        def helper(i, j, visited_set, current_wt, current_word):
            if None in current_wt:
                result.add(current_word)
            if (
                (i, j) in visited_set
                or i >= len(board)
                or j >= len(board[0])
                or i < 0
                or j < 0
            ):
                return

            char = board[i][j]
            if char not in current_wt:
                return
            visited_set.add((i, j))
            current_word += char

            move_list = [
                (i, j - 1),
                (i - 1, j),
                (i + 1, j),
                (i, j + 1),
            ]
            for x in move_list:
                helper(x[0], x[1], visited_set.copy(), current_wt[char], current_word)

        wt = make_trie(words)

        result = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                helper(i, j, set(), wt, "")
                for r in result:
                    delete_from_trie(wt, r)

        return list(result)
