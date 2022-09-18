class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self_ans = []
        self.permuteHelper(nums, 0, len(nums), self_ans)
        return self_ans
    
    def permuteHelper(self, nums, start, end, result):
        if start==end:
            if nums not in result:
                result.append(list(nums))
            return 
        for i in range(start, end):
            arr = self.swap(nums, i, start)
            self.permuteHelper(nums, start+1, end, result)
            arr = self.swap(nums, i, start)
            
    def swap(self, nums, start, end):
        if start == end:
            return nums
        nums[start], nums[end] = nums[end], nums[start]
        return nums
        