class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        result = []
        noOfLines = 1
        total = 0
        for letter in s:
            letterValue = widths[ord(letter) - ord('a')]
            total+=letterValue
            if total > 100:
                total = letterValue
                noOfLines+=1
        return [noOfLines, total]
                
        