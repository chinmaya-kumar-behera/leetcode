from typing import *

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        zigzag = [''] * numRows
        row = 0
        direction = 1
        
        for char in s:
            zigzag[row] += char
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            row += direction
        
        return ''.join(zigzag)


# PAHNAPLSIIGYIR

s = "PAYPALISHIRING"

obj = Solution()
result = obj.convert(s, numRows = 3)
print(result)

        
# # P   A   H   N
# # A P L S I I G
# # Y   I   R