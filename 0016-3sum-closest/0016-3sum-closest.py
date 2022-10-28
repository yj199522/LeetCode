class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        curr_sum = 0
        i,k = 0,len(nums)-1
        j = i+1
        minimum_sum = 100000000
        nums = sorted(nums)

        while i < k:
            j = i + 1

            while j < k:                
                curr_sum = nums[i] + nums[j] + nums[k]

                if curr_sum == target:
                    return curr_sum

                elif curr_sum > target:
                    k-=1
                elif curr_sum < target:
                    j+=1

                if abs(target - curr_sum) < abs(target - minimum_sum):
                    minimum_sum = curr_sum

            i += 1
            k = len(nums) - 1
        return minimum_sum