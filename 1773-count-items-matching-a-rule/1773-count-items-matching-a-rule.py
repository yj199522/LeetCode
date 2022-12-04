class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keys = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        result = 0
        indexOfKey = keys[ruleKey]
        for item in items:
            if item[indexOfKey] == ruleValue:
                result+=1
        return result
            
        