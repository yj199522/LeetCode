class Solution:
    def canJump(self, nums: List[int]) -> bool:
        flag=True
        n = len(nums)
        for i in range(n):
            if nums[i]==0 and i!=n-1:
                flag=False
                for j in range(i-1,-1,-1):
                    if nums[j]>=i-j+1:
                        flag=True
                        break
            if not flag:
                return False
        return flag
        