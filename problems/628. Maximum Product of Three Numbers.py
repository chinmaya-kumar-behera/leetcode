class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        max1 = nums[-1] * nums[-2] * nums[-3]
        max2 = nums[0] * nums[1] * nums[-1]


print(Solution().maximumProduct([1,2,3,4]))
        