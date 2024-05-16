from typing import *

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s,t))) == len(set(t)) == len(set(s))
    
print(Solution.isIsomorphic(Solution(),'egg','add'))