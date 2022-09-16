class Solution:
    def reverse(self, x: int) -> int:
        result, sign = 0, (-1 if x<0 else 1)
        x = x*sign
        while x > 0:
            digit = x%10
            result = result*10 + digit;
            x = x//10
            if (-2**31) > sign*result  or sign*result > (2**31 - 1):
                return 0
        return sign*result 
        