class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        width = 0
        for char in s:
            w = widths[ord(char) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w
        return [lines, width]
                
        