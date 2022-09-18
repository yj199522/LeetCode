class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        def dfs(i, res, sum_val):
            if sum_val == target:
                sol.append(res.copy())
                return
            if sum_val > target or i >= len(candidates):
                return
            res.append(candidates[i])
            sum_val += candidates[i]
            dfs(i, res, sum_val) 
            data = res.pop()
            sum_val -= data
            dfs(i + 1, res, sum_val)
        dfs(0, [], 0)
        return sol
        