class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            return 0 if nums[-1] == target else -1
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if target < nums[mid] or target > nums[right]:
                    right=mid-1
                else:
                    left=mid+1
        return -1
                    