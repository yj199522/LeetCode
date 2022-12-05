class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        print(len(words1), len(words2))
        if len(words2) < len(words1):
            words1, words2 = words2, words1
        result = 0
        for word in words1:
            if word in words2 and words1.count(word) == words2.count(word) == 1:
                result+=1
        return result
        