class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, result = 0, len(nums) - 1, []
        
        while left<= right:
            leftValue = nums[left] ** 2
            rightValue = nums[right] ** 2
            
            if abs(nums[left]) >= abs(nums[right]):
                result.append(leftValue)
                left+=1
            else:
                result.append(rightValue)
                right-=1
        return result[::-1]
        