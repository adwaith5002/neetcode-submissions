class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patterns=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i]+"*"+word[i+1:]
                patterns[pattern].append(word)

        q=deque()
        q.append(beginWord)
        visit=set([beginWord])
        count=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return count
                for j in range(len(word)):
                    pattern=word[:j] + "*" + word[j+1:]
                    for child in patterns[pattern]:
                        if child not in visit:
                            visit.add(child)
                            q.append(child)
            count+=1

        return 0