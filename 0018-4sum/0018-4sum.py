class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        start = 0
        result = []
        nums = sorted(nums)
        while start < len(nums) - 3:
            while start > 0 and nums[start] == nums[start-1] and start < len(nums) - 3:
                start+=1
            i = start+1
            while i < len(nums) - 2:
                while i > start+1 and nums[i] == nums[i-1] and i < len(nums) - 2:
                    i+=1
                left, right = i+1, len(nums)-1
                while left < right:
                    total = nums[start] + nums[i] + nums[left] + nums[right]
                    if total < target:
                        left+=1
                    elif total > target:
                        right-=1
                    else:
                        result.append([nums[start], nums[i], nums[left], nums[right]])
                        left+=1
                        while nums[left] == nums[left-1] and left<right:
                            left+=1
                i+=1
            start+=1
        return result
        