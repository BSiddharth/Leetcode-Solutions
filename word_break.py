# https://leetcode.com/problems/word-break/description/
# git add . && git commit -m "completed word_break" && git push && exit

from typing import List
import functools

class Solution:
    def make_trie(self,wordlist):
        trie = {}

        for word in wordlist:
            current_trie = trie
            for ch in word:
                if ch not in current_trie:
                    current_trie[ch] = {}
                current_trie = current_trie[ch]
            current_trie[None] = None
        
        return trie

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = self.make_trie(wordDict)
        slen = len(s)
        
        @functools.cache
        def helper(start):
            current_trie = trie
            while start != slen:
                current_char = s[start]
                if current_char not in current_trie:
                    return False
                if None in current_trie[current_char]:
                    if start == slen-1 or helper(start+1):
                        return True
                current_trie = current_trie[current_char]
                start += 1

            return False
        return helper(0)
