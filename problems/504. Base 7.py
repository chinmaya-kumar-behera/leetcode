class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        s = ""
        t = num
        num = abs(num)
        while num != 0:
            s += str(num % 7)
            num = num // 7
        
        if t < 0:
            s += '-'
        s = s[::-1]
        return s
    
solution = Solution()
print(solution.convertToBase7(100))  # Output: "202"
print(solution.convertToBase7(-7))  