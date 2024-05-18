from typing import *
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numSet = set(nums)
        newl = []
        for i in range(1,len(nums)+1):
            if i not in numSet:
                newl.append(i)
        return newl
    
        # or 
        set1 = set(nums)
        set2 = set(range(1,len(nums)+1))
        return list(set2.difference(set1))
    

print(Solution().findDisappearedNumbers([1,1]))