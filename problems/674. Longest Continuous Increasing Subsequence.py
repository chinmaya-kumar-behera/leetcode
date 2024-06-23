class Solution(object):
    def findLengthOfLCIS(self, nums):
        newl = [nums[0]]
        max = 1
        for n in nums[1:]:
            if n <= newl[-1]:
                if len(newl) > max:
                    max = len(newl)
                newl = [n]
            else:
                newl.append(n)
        
        if len(newl) > max:
            max = len(newl)

        return max



print(Solution().findLengthOfLCIS([2,2,2,2,2]))