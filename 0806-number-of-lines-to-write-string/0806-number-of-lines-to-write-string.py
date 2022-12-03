class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        k = 1
        l = 0
        for c in s:
            w = widths[ord(c) - ord('a')]
            l += w
            if l > 100:
                k += 1
                l = w
        return [k, l]
                
        