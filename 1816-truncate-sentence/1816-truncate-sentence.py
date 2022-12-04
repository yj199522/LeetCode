class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        words = s.split(' ')[:k]
        return ' '.join(words)
        