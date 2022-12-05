class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = sum(1 for word in words if word[:len(pref)] == pref)
        return result
            
        