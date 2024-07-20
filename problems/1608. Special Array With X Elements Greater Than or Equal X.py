class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for x in range(1, len(nums) + 1):
            if len([num for num in nums if num >= x]) == x:
                return x
        return -1


        