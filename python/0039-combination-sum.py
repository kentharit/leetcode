from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        comb = []
        cursum = 0

        def dfs(i):
            nonlocal cursum
            if cursum == target:
                res.append(comb.copy())
                return
            
            if cursum > target or i >= len(candidates):
                return

            comb.append(candidates[i])
            cursum += candidates[i]
            dfs(i)
            comb.pop()
            cursum -= candidates[i]

            dfs(i + 1)
        dfs(0)
        return res