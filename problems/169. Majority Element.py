class Solution:
    def majorityElement(self, nums):
        newl = []
        count = 0
        hf = 0

        for n in nums:
            if n not in newl:
                if count < nums.count(n):
                    count = nums.count(n)
                    hf = n
                newl.append(n)
        return hf
    
print(Solution().majorityElement([3,2,3]))