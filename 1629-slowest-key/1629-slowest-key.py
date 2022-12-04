class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maximumValue = releaseTimes[0]
        result = keysPressed[0]
        for index in range(1, len(releaseTimes)):
            difference = releaseTimes[index] - releaseTimes[index-1]
            if difference >= maximumValue:
                if difference == maximumValue and keysPressed[index] > result:
                    result = keysPressed[index]
                elif difference > maximumValue:
                    result = keysPressed[index]
                maximumValue = difference
        return result
                    
        