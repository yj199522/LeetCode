class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self._ans = []
        self.permutationHelper(nums,0,len(nums), self._ans)
        return self._ans
    
    def permutationHelper(self, nums, start, end, result):
        if start==end:
            if nums not in result:
                result.append(list(nums))
            return
        
        for i in range(start, end):
            arr = self.swap(nums, i, start)
            self.permutationHelper(nums, start+1,end, result)
            arr = self.swap(nums, i, start)
            
    def swap(self, nums, start, end):
        if start == end:
            return nums
        nums[start], nums[end] = nums[end], nums[start]
        return nums