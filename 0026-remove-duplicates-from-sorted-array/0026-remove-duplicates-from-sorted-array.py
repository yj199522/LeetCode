class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = len(nums)-1
        while idx > 0:
            if nums[idx] == nums[idx-1]:
                nums.pop(idx)
            idx = idx-1
        