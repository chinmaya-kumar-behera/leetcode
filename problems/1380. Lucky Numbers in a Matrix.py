from typing import *

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        rowMins = {min(arr) for arr in matrix}
        colMax = {max(arr) for arr in zip(*matrix)}

        return list(rowMins & colMax)
    
arr1 = [[3,7,8],[9,11,13],[15,16,17]]
arr2 = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
arr3 = [[7,8],[1,2]]

print(Solution().luckyNumbers(arr1))
        