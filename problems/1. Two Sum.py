class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind in range(len(nums)-1):
            if nums[ind]+nums[ind+1] == target:
                return [ind,ind+1]