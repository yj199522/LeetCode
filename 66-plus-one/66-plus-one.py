class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 2
        value = digits[-1] + 1
        result = []
        carry = value // 10
        value = value % 10
        result.append(value)
        while i >= 0:
            value = digits[i] + carry
            carry = value // 10
            value = value % 10
            result.append(value)
            i-=1
        if carry:
            result.append(carry)
        return result[::-1]