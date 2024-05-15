from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return nums



obj = Solution()

l1 = [3,2,2,3]
val = 3
res = obj.removeElement(l1,val)
print(res)