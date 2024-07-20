from typing import *

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxDepth = 0

        for ch in s:
            if ch == "(":
                depth += 1
                if depth > maxDepth:
                    maxDepth = depth
            elif ch == ")":
                depth -= 1
            
        return maxDepth


s1 = "(1+(2*3)+((8)/4))+1"
s2 = "(1)+((2))+(((3)))"
s3 = "()(())((()()))"

print(Solution().maxDepth(s2))