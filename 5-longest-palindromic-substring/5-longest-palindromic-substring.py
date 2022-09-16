class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s, l, r): 
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[(l+1):r]
        
        res = ''
        i=0
        while i<len(s):
            s1 = palindrome(s,i,i)#Find palindrome when center is i (odd number of words)
            s2 = palindrome(s,i,i+1)#find palindrome when center is i and i+1 (even number of words)
            if len(s1)>len(s2):
                if len(s1)>len(res):
                    res = s1
            else:
                if len(s2)>len(res):
                    res = s2
            i+=1
        return res
        