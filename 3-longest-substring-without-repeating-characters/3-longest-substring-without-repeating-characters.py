class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, result = 0, 0, 0
        sub = ''
        while right < len(s):
            if s[right] in sub:
                left+=1
                right=left
                sub = ''
            else:
                sub+=s[right]
                right+=1
                result = max(result, right - left)
        return result
            
        