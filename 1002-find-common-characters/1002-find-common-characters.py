class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) < 2:
            return A
        
        firstWord = set(A[0])
        result = []
        for letter in firstWord:
            minValue = min([word.count(letter) for word in A])
            if minValue:
                result+=[letter]*minValue
        return result

        
        