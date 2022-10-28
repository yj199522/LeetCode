class Solution:
    def startPoint(self, nums, target):
        return self.conditionCheck(nums, target, 'start')
    
    def endPoint(self, nums, target):
        return self.conditionCheck(nums, target, 'end')
    
    def checking(self, mid, nums, target, types):
        if nums[mid] == target:
            if types == 'start':
                while mid > 0 and nums[mid] == nums[mid-1]:
                    mid -=1
            else:
                while mid < len(nums) - 1 and nums[mid] == nums[mid+1]:
                    mid +=1
            return 'found', mid
        elif nums[mid] < target:
            return 'left', -1
        return 'right', -1
            
    
    def conditionCheck(self, nums, target, types):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            condition, found = self.checking(mid, nums, target, types)
            if condition == 'found':
                return found
            elif condition == 'left':
                left = mid + 1
            else:
                right = mid - 1
        return -1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.startPoint(nums, target), self.endPoint(nums, target)]
        
        