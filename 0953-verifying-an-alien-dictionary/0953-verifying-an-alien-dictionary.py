class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {c : i for i, c in enumerate(order)}        
        words = [[mp[c] for c in word] for word in words]
        return all(word1 <= word2 for word1, word2 in zip(words, words[1:]))
        