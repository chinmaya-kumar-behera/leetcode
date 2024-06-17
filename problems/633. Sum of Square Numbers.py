from typing import *
from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))

        while a <= b :
            exp = a**2 + b**2

            if exp == c:
                return True
            elif exp < c:
                a += 1
            else:
                b -= 1

        return False
            

n1 = 5
n2 = 3

print(Solution().judgeSquareSum(4))