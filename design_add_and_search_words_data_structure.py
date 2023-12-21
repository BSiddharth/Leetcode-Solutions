# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
# git add . && git commit -m "completed design_add_and_search_words_data_structure" && git push && exit


class WordDictionary:
    def __init__(self):
        self.wd = {}

    def addWord(self, word: str) -> None:
        current_wd = self.wd

        for i in range(len(word)):
            if word[i] not in current_wd:
                current_wd[word[i]] = {}
            current_wd = current_wd[word[i]]
        current_wd[None] = None

    def search(self, word: str) -> bool:
        def helper(i, current_wd):
            if i == len(word):
                return None in current_wd
            if word[i] == ".":
                return any(
                    map(
                        lambda x: helper(i + 1, current_wd[x])
                        if x is not None
                        else False,
                        current_wd.keys(),
                    )
                )
            else:
                if word[i] not in current_wd:
                    return False
                else:
                    return helper(i + 1, current_wd[word[i]])

        return helper(0, self.wd)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
