class Solution:
    def tribonacci(self, n):
        fibo = [0,1,1]
        if n <= 2:
            return fibo[n]
        else:
            while len(fibo) < n+1:
                fibo.append(fibo[-1]+fibo[-2]+fibo[-3])
        return fibo[n]


print(Solution().tribonacci(4))

