class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        total = len(grid) * len(grid[0])

        numSet = []

        for numArr in grid:
            numSet.extend(numArr)

        res = []
        nums = [*range(1,total+1)]

        for n in nums:
            if n not in numSet:
                res.append(n)
            else:
                numSet.remove(n)

        return [*numSet, *res] 
    
print(Solution().findMissingAndRepeatedValues([[1,3],[2,2]]))
                



        

        




        