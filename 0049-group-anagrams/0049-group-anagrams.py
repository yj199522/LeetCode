class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None or len(strs) < 2:
            return [strs]
        result = {}
        for i in strs:
            data = ''.join(sorted(i))
            if data not in result:
                result[data] = [i]
            else:
                result[data].append(i)
        return result.values()
        