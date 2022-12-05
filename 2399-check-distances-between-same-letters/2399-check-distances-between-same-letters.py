class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        letterList = set(s)
        for letter in letterList:
            spacing = distance[ord(letter) - ord('a')]
            indexInString = s.index(letter)
            if indexInString + spacing + 1 >= len(s) or s[indexInString] != s[indexInString + spacing + 1]:
                return False
        return True
        