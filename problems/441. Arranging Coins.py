class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        row = 0
        left = n
        while left > row:
            row += 1
            n -= row
            left -= row
            k += 1

        return k
    
        # or
        return int((sqrt(8 * n + 1) - 1) / 2)
    
print(Solution().arrangeCoins(8))