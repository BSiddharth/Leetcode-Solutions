# https://leetcode.com/problems/word-ladder/description/
# git add . && git commit -m "completed word_ladder" && git push && exit

from collections import deque
from typing import DefaultDict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        
        neighbours = DefaultDict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                neighbours[pattern].append(word)

        queue = deque()
        queue.append(beginWord)
        result = 1
        seen_words = set([beginWord])
        while queue:
            for _ in range(len(queue)):
                current_word = queue.popleft()

                if current_word == endWord:
                    return result
                
                for i in range(len(current_word)):
                    print(current_word[:i] , '*' , current_word[i+1:])
                    pattern = current_word[:i] + '*' + current_word[i+1:]
                    for word in neighbours[pattern]:
                        if word in seen_words:
                            continue
                        seen_words.add(word)
                        queue.append(word)
                            

            result += 1

        return 0


