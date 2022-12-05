class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # start = 0
        # index = 0
        # while start < len(s) and index < len(words):
        #     word = words[index]
        #     lenOfWord = len(word)
        #     if s[start:start+lenOfWord] == word:
        #         index+=1
        #         start+=lenOfWord
        #     else:
        #         return False
        # return start == len(s)
        for i in range(len(words) + 1):
            if len(words) == 1:
                if s == words[0]:
                    return True
            if "".join(words[:i]) == s:
                return True
        return False
            
            
        