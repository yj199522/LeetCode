class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # left, right = 0, 1
        # while left < right and right < len(words):
        #     sortLeftWord, sortrightWord = sorted(words[left]), sorted(words[right])
        #     if sortLeftWord == sortrightWord:
        #         words.pop(right)
        #     else:
        #         left, right = right, right + 1
        # return words
        start = 0
        while start < len(words) -1:
            if sorted(words[start]) == sorted(words[start+1]):
                words.remove(words[start+1])
                continue
            start+=1
        return words
                
            
            
        
        