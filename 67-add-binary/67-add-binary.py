class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        n, m = len(a) - 1, len(b) - 1
        while n>=0 and m>=0:
            value = int(a[n]) + int(b[m]) + carry
            carry = value//2
            value %=2
            result+=str(value)
            n-=1
            m-=1
        
        while n>=0:
            value = int(a[n]) + carry
            carry = value//2
            value %=2
            result+=str(value)
            n-=1
        
        while m>=0:
            value = int(b[m]) + carry
            carry = value//2
            value %=2
            result+=str(value)
            m-=1
        
        if carry:
            result+=str(carry)
        
        return result[::-1]
            
        