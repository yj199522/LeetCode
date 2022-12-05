class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWord = -1
        for sentence in sentences:
            splitSent = len(sentence.split(' '))
            if  splitSent > maxWord:
                maxWord = splitSent
        return maxWord
        