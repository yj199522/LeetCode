class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboardLetterAsPerRow = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]
        result = []
        
        for word in words:
            row = 0
            typeWord = ''
            searchRow = -1
            for letter in word:
                while row < len(keyboardLetterAsPerRow) and searchRow < 0:
                    if letter.lower() in keyboardLetterAsPerRow[row]:
                        searchRow = row
                    else:
                        row+=1
                if letter.lower() not in keyboardLetterAsPerRow[searchRow] and searchRow != -1:
                    break
                else:
                    typeWord+=letter
            if typeWord == word:
                result.append(word)
                
        return result
                        
                    
        