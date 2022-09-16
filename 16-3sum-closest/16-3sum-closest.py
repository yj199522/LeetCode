class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = math.inf
        for i in range(len(nums)):
            j = i + 1
            k = len(nums)-1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if abs(three_sum - target) < diff:
                    ans = three_sum
                    diff = abs(three_sum - target)
                if diff == 0:
                    break
                if three_sum < target:
                    j += 1
                else:
                    k -= 1
        return ans
        