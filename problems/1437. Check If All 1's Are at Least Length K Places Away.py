class Solution():
    def kLengthApart(self, nums, k):
        one = False
        count = 0
    
        for num in nums:
            if num == 1:
                if one is False:
                    one = True
                else:
                    if count < k:
                        return False
                    else:
                        count = 0
                    
            else:
                if one:
                    count += 1

        return True
    
print(Solution().kLengthApart([1,0,0,0,1,0,1],2))