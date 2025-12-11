class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(deque)
        for word in words:
            waiting[word[0]].append(word)
        
        count = 0
        for c in s:
            words_waiting = waiting[c]
            waiting[c] = deque()
            while words_waiting:
                word = words_waiting.popleft()
                if len(word) == 1:
                    count += 1
                else:
                    waiting[word[1]].append(word[1:])
        return count