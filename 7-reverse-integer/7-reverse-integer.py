class Solution:
    def reverse(self, x: int) -> int:
        negative = True if x < 0 else False
        x = str(x)
        if negative:
            sign = x[0]
            number = x[1:][::-1]
            x = sign + number
            ''.join(x)
            x = int(x)
        else:
            x = x[::-1]
            x = ''.join(x)
            x = int(x)
        
        if -(2**31) <= x <= (2**31) - 1:
            return x
        
        return 0