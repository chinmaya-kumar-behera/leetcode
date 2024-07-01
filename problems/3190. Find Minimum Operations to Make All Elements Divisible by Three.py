class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for num in nums:
            if num % 3 == 0:
                continue
            
            if  (num + 1) % 3 == 0 or (num - 1) == 0 or (num-1) % 3 == 0:
                count += 1
        return count

        

# or


class Solution1(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in nums:
            if i%3!=0:
                c+=1
        return c
                