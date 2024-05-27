class Solution:
    def thirdMax(self, nums):
        l = sorted(set(nums),reverse=True)

        if len(l) >= 3:
            return l[2]
        else:
            return l[0]