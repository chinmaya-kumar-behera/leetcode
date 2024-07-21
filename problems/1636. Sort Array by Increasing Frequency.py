from typing import *
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

        nums.sort(key=lambda x: (m[x],-x))
        
        return nums


arr = [1,1,2,2,2,3] 

print(Solution().frequencySort(arr))