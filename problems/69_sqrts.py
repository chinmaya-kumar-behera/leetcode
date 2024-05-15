class Solution:
    def mySqrt(self, x):
        n = 1
        while n*n <= x:
            n+=1
        if n*n == x:
            return n
        else:
            return n-1

obj = Solution();

print(obj.mySqrt(8))