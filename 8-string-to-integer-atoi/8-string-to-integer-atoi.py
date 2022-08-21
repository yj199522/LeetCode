class Solution:
    def myAtoi(self, s: str) -> int:
        allow = ["+","-"]
        result = ''
        for i in s:
            if i == ' ' and len(result)==0:
                continue
            elif i in allow and len(result)==0:
                result+=i
            elif i.isdigit():
                result+=i
            else:
                break
        if not result or result in allow:
            return 0
        result = int(result)
        if -2**31 <= result <= 2**31 - 1:
            return result
        elif result < 0:
            return -2**31
        else:
            return 2**31 -1