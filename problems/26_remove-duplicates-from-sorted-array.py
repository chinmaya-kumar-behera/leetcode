from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1

        return l


    

obj = Solution()
l1 = [1,1,2]
l2 = [0,0,1,1,1,2,2,3,3,4]
res = obj.removeDuplicates(l1)

print(res)