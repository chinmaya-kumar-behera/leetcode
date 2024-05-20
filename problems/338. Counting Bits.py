class Solution:
    def countBits(self, n: int) -> List[int]:
        return [*map(lambda i:bin(i)[2:].count('1') ,range(n+1))]
        
        