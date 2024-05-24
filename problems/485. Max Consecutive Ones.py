class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # return "".join(map(str,nums))
        return max(map(len,"".join(map(str,nums)).split("0")))
    
print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))