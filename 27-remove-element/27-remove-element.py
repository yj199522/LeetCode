class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = len(nums)-1
        while idx >= 0:
            if nums[idx] == val:
                nums.pop(idx)
            idx = idx-1
        