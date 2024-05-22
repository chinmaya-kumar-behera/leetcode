from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        
        for i in range(len(nums) + 1):
            if i not in s:
                return i

    
print(Solution().missingNumber([3,0,1]))
print(Solution().missingNumber([0,1]))
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))