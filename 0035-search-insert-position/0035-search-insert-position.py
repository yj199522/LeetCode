class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,v in enumerate(nums):
            if target<=v:
                return i
        return len(nums)
        