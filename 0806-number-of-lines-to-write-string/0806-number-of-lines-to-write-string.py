class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        result = []
        noOfLines = 1
        start = 0
        total = 0
        while start < len(s):
            orderOfChar = ord(s[start]) - ord('a')
            letterValue = widths[orderOfChar]
            total+=letterValue
            if total > 100:
                total = letterValue
                noOfLines+=1
            start+=1
        return [noOfLines, total]
                
        