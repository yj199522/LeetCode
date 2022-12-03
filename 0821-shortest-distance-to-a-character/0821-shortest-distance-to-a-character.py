class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = [0] * len(s)
        indexOfChar = s.index(c)
        for index in range(len(s)):
            if abs(indexOfChar - index) > abs(s.find(c,index) - index):
                indexOfChar = s.index(c, index)
            if s[index] !=c:
                result[index] = abs(index - indexOfChar)
            else:
                result[index] = 0
        return result
        