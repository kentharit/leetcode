from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy
        
        perms = self.permute(nums[1:])

        for perm in perms:
            for i in range(len(perm) + 1): 
                p_copy = perm.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res