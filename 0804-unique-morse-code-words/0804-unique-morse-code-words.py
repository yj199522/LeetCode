class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCodeList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        if len(words) < 2:
            return len(words)
        result = []
        minValue = ord('a')
        for word in words:
            morseCodeString = ''
            for letter in word:
                indexToFindMorseCode = ord(letter) - minValue
                morseCodeString+=morseCodeList[indexToFindMorseCode]
            if morseCodeString not in result:
                result.append(morseCodeString)
        return len(result)
                