from typing import *
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

s1 = "Hello, my name is John"
s2 = 'hello'

print(Solution().countSegments(s1))
