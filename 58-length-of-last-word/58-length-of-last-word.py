class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) == 1:
            return 1
        data = s.split(' ')
        n = len(data) - 1
        while n >= 0:
            if len(data[n]) > 0:
                return len(data[n])
            n-=1
        return 0
        