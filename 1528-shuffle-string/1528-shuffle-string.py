class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ['-'] * len(s)
        for index, value in enumerate(indices):
            result[value]=s[index]
        return ''.join(result)
        