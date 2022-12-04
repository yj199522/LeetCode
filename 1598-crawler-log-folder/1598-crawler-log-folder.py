class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = []
        for log in logs:
            countOfDots = log.count('.')
            if countOfDots == 2:
                if len(result):
                    result.pop()
            elif countOfDots == 0:
                result.append(log.split('/')[0])
        return len(result)
        