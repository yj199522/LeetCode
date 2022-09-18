class Solution:
    def leftCondition(self, nums, mid, target):
        if nums[mid] == target:
            if mid > 0 and target == nums[mid-1]:
                return 'left'
            else:
                return 'found'
        elif target < nums[mid]:
            return 'left'
        else:
            return 'right'
            
    def rightCondition(self, nums, mid, target):
        if nums[mid] == target:
            if mid < len(nums) - 1 and target == nums[mid+1]:
                return 'right'
            else:
                return 'found'
        elif target < nums[mid]:
            return 'left'
        else:
            return 'right'
    
    def binarySearch(self, nums, target, types):
        left, right = 0, len(nums) - 1
        while left<= right:
            mid = (left + right) //2
            condition = self.leftCondition(nums, mid, target) if types == 'left' else self.rightCondition(nums, mid, target)
            if condition == 'found':
                return mid
            elif condition == 'left':
                right = mid - 1
            else:
                left = mid + 1
        return -1
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums is None and len(nums) == 0:
            return [-1, -1]
        return [self.binarySearch(nums, target, 'left'), self.binarySearch(nums, target, 'right')]
            
        
        