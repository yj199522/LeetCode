class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for word in words:
            # checkIfWordPresent = all(letter in char  for letter in word)
            temp = list(chars)
            checkIfWordPresent = True
            for letter in word:
                if letter in temp:
                    temp.pop(temp.index(letter))
                else:
                    checkIfWordPresent = False
                    break
            if checkIfWordPresent:
                result+=len(word)
        return result
        