class Solution:
    def isPalindrome(self, x: int) -> bool:
        if 0<= x <=9:
            return True
        if x < 0:
            return False
        
        result = 0
        temp = x
        while temp:
            result = result * 10 + temp%10
            temp = temp//10
        
        return result == x
        