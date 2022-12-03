class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        wordContainInPlate = {}
        for letter in licensePlate:
            if letter.isalpha():
                letterLower = letter.lower()
                if letterLower not in wordContainInPlate:
                    wordContainInPlate[letterLower] = 1
                else:
                    wordContainInPlate[letterLower]+=1
        result = 'dafsaffafsafssd'
        for word in words:
            flag = True
            for keys in wordContainInPlate:
                wordCount = word.count(keys)
                if wordCount < wordContainInPlate[keys]:
                    flag = False
                    break
            if flag:
                if len(result) > len(word):
                    result = word
        return result
                
            
        