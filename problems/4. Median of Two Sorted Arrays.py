class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        newl = nums1 + nums2
        newl.sort()
        n = len(newl)

        if n%2 == 1:
            return newl[n //2]
        else:
            return (newl[(n//2)-1] + newl[n//2]) / 2.0

b1 = [1,2]
b2 = [3,4]


print(Solution().findMedianSortedArrays(b1,b2))