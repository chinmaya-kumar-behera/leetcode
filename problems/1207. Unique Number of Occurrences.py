class Solution:
    def uniqueOccurrences(self, arr):
        checked = []
        counter = []

        for num in arr:
            if num not in checked:
                checked.append(num)
                count = arr.count(num)
                if count in counter:
                    return False
                else:
                    counter.append(count)
        return True
            




l1 = [1,2,2,1,1,3]
l2 = [1,2]
l3 = [-3,0,1,-3,1,1,1,-3,10,0]
print(Solution().uniqueOccurrences(l3))
        