class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        s += "@"
        prev = s[0]
        count = 1
        si = 0
        groups = []
    
        for ch in s[1:]:
            if ch == prev[-1]:
                prev += ch
                count += 1
            else:
                if count >= 3:
                    groups.append([si,si+(count-1)])
                prev = ch
                si += count
                count = 1
                    
        return groups
    
print(Solution().largeGroupPositions('abc'))
# print(Solution().largeGroupPositions('abbxxxxzzy'))