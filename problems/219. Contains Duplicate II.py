class Solution:
    def containsNearbyDuplicate(self, nums, k):
        num_dict = {}
        for i, num in enumerate(nums):
            if num in num_dict and i - num_dict[num] <= k:
                return True
            num_dict[num] = i
        return False

            
l = [1,0,1,1]
k1 = 1
print(Solution().containsNearbyDuplicate(l,k1))


print()
