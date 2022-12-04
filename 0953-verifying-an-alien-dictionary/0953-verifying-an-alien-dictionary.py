class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lookup = {char:index for index, char in enumerate(order)}
        words2 = []
        for word in words:
            temp = []
            for letter in word:
                temp.append(lookup[letter])
            words2.append(temp)
        for index in range(1, len(words2)):
            if words2[index-1] > words2[index]:
                return False
        return True
        