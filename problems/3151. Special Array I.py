class Solution:
    def isArraySpecial(self, nums):
        pairs = [(nums[ind]%2 == 0,nums[ind+1]%2 == 0) for ind in range(len(nums)-1)]
        res = list(map(lambda var: var[0] ^ var[1], pairs))
        return all(res)


l1 = [2,1,4]
print(Solution().isArraySpecial(l1))