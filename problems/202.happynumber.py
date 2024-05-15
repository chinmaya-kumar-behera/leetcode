from typing import *


class Solution:
    def isHappy(self, n: int) -> bool:
        sq = n**n
        sum = 0

        while sq < 9 :
            
            while sq!=0:
            sum += sq%10
            sq //= 10

        
        