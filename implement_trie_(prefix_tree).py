# https://leetcode.com/problems/implement-trie-(prefix-tree)/description/
# git add . && git commit -m "completed implement_trie_(prefix_tree)" && git push && exit


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        current_trie = self.trie
        for i in range(len(word)):
            if word[i] in current_trie:
                current_trie = current_trie[word[i]]
                continue
            current_trie[word[i]] = {}
            current_trie = current_trie[word[i]]

        current_trie[None] = None

    def search(self, word: str, startsWith=False) -> bool:
        current_trie = self.trie
        for i in range(len(word)):
            if word[i] not in current_trie:
                return False

            current_trie = current_trie[word[i]]

        if startsWith:
            return True
        else:
            return None in current_trie

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, startsWith=True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
