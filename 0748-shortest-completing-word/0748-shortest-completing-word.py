class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        wordContainInPlate = {}
        licensePlate = licensePlate.lower()
        for letter in licensePlate:
            if letter.isalpha():
                if letter not in wordContainInPlate:
                    wordContainInPlate[letter] = 1
                else:
                    wordContainInPlate[letter]+=1
        result = ''
        for word in words:
            flag = True
            for keys in wordContainInPlate:
                wordCount = word.count(keys)
                if wordCount < wordContainInPlate[keys]:
                    flag = False
                    break
            if flag:
                if len(result) == 0 or len(result) > len(word):
                    result = word
        return result
                
            
        