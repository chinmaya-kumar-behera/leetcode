class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        reminder = 0
        for i in range(len(nums)):
            reminder += nums[i]
            reminder %= k
            if reminder not in d:
                d[reminder] = i
            elif i - d[reminder] >= 2:
                return True

        return False