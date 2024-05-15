# from typing import 

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
        

obj = Solution();
a= '11'
b = '1'
print(obj.addBinary(a,b))