class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        result = 0
        for word in words1:
            if words1.count(word) == words2.count(word) == 1:
                result+=1
        return result
        