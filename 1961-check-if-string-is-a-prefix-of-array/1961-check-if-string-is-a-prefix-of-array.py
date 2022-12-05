class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        start = 0
        index = 0
        while start < len(s) and index < len(words):
            word = words[index]
            lenOfWord = len(word)
            if s[start:start+lenOfWord] == word:
                index+=1
                start+=lenOfWord
            else:
                return False
        return start == len(s)
            
            
        