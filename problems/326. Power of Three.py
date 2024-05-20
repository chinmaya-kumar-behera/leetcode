class Solution:
    def isPowerOfThree(self, n):
        
        num = 1

        while 3**num < n:
            num+=1
        
        print(num)
        return 3**num == n

        
print(Solution().isPowerOfThree(27))