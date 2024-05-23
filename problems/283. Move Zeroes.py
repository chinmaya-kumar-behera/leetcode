class Solution:
    def moveZeroes(self, nums):
        """ 
        Do not return anything, modify nums in-place instead.
        """
        
        for num in nums:
            if num == 0:
                nums.remove(0)
                nums.append(0)

        print(nums)

Solution().moveZeroes([0,1,0,3,12])
        