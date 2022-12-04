class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ops = 0
        for i in logs:
            if '.' not in i:
                ops += 1
            elif ops > 0 and i == '../':
                ops -= 1
        return ops
        