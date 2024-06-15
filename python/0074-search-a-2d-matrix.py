from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix[0])
        height = len(matrix)
        l, r = 0, length * height - 1

        while l <= r: 
            mid = (l + r) // 2
            row = int(mid/length)
            col = mid % length

            element_mid = matrix[row][col]

            if target > element_mid:
                l = mid + 1
            elif target < element_mid: 
                r = mid - 1
            else:
                return True
        return False
