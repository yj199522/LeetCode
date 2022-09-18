class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_end_here = nums[0]
        #start_p = 0
        largest_til_here = nums[0]
        #start = 0
        #end = 0
        for i in range(1, len(nums)):
            if largest_end_here + nums[i] < nums[i]:
                largest_end_here = nums[i]
                #start_p = i
            else:
                largest_end_here += nums[i]
            if largest_til_here < largest_end_here:
                largest_til_here = largest_end_here
                #start = start_p
                #end = i
        #print(nums[start:end+1])
        return largest_til_here
        
            
         
        