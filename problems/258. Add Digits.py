from functools import reduce

class Solution:
    def addDigits(self, num):
        
        while num > 9:
            num = reduce(lambda a,b:a+int(b),str(num),0)
        
        return num
        

print(Solution().addDigits(38))