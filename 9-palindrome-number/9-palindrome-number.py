class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        result = 0
        while temp:
            val = temp % 10
            result = result * 10 + val
            temp = temp // 10
        return result == x