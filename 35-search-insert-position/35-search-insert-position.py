class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if target > nums[mid]:
            return mid + 1
        else:
            return mid
        