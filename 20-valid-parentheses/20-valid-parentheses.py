class Solution:
    def isValid(self, s: str) -> bool:
        search = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        
        result = []
        
        if s is None or s[0] not in search:
            return False
        
        for i in s:
            if i in search:
                result.append(search[i])
            else:
                if len(result) > 0:
                    topValue = result.pop()
                    if topValue != i:
                        return False
                else:
                    return False
        if len(result) == 0:
            return True
        return False