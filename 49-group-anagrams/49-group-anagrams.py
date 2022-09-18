class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return []
        dic = {}
        for i in strs:
            data = ''.join(sorted(i))
            if data not in dic:
                dic[data] = [i]
            else:
                dic[data].append(i)
        return dic.values()
        