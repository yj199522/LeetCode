class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j, n = 0, 0, 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                n+=1
            else:
                i = i - j + 1
                j = 0
                n = 0
            if n == len(needle):
                return i - j
        return -1
        