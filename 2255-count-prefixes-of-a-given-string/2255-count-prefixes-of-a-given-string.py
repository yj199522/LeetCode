class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        result=0
        for index in range(len(s)):
            string = s[:index+1]
            if string in words:
                result+=words.count(string)
        return result
        