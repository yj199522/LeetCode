class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left, right, n = 0, len(height) - 1, len(height) - 1
        while left<right:
            totalWater = min(height[left], height[right]) * n
            maxWater = max(totalWater, maxWater)
            if height[left] <=  height[right]:
                left+=1
            else:
                right-=1
            n-=1
        return maxWater
        
        