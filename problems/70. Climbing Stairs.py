# class Solution:
#     def climbStairs(self, n):
#         if n == 1:
#             return 1

#         l = [0]*(n+1)
#         l[1] = 1
#         l[2] = 2

#         for ind in range(3,n+1):
#             l[ind] = l[ind-1]+l[ind-2]

#         return l[n]


# obj = Solution()
# n = 10
# print(obj.climbStairs(8));


class Solution:
    def climbStairs(self, n):
        dp = [None] * (n + 1)

        def helper(n):
            if n <=2 :
                return n

            if dp[n] is None:
                dp[n] = helper(n-1)+helper(n-2)
            return dp[n]
           
        
        return helper(n)

print(Solution().climbStairs(5))