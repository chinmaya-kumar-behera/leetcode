class Solution:
    def relativeSortArray(self, arr1, arr2):
        result = []
        others = []
        tempArr = []

        arrDict = {}

        for num in arr1:
            if num in arr2:
                if num not in tempArr:
                    tempArr.insert(0,num)
            else:
                others.insert(0,num)

            if num not in arrDict:
                arrDict[num] = arr1.count(num)

        for num in arr2:
            result.extend([num]*arrDict[num])

        result.extend(sorted(others))
            
        return result



arr1 = [2,3,1,3,2,4,6,7,9,2,19] 
arr2 = [2,1,4,3,9,6]

# Output: [2,2,2,1,4,3,3,9,6,7,19]


print(Solution().relativeSortArray(arr1,arr2))
        