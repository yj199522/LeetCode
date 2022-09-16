class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        largest_so_far = 0
        for i in range(len(s)-1,-1,-1):                
            if d[s[i]] < largest_so_far:
                num-=d[s[i]]
            else:
                num+=d[s[i]]
                largest_so_far = d[s[i]]
                
        return num
        