class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]: return i
        return ''
#         for word in words:
#             if self.isPalindrome(word):
#                 return word
#         return ''
    
#     def isPalindrome(self, word) -> bool:
#         left, right = 0, len(word) - 1
#         while left < right:
#             if word[left] != word[right]:
#                 return False
#             left+=1
#             right-=1
#         return True
        
        