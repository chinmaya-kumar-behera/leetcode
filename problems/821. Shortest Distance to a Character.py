class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        c_positions = []

        for ind in range(len(s)):
            if s[ind] == c:
                c_positions.append(ind)


        arr = [0]*len(s)

        for i in range(len(s)):
            if s[i] != c:
                arr[i] = min(abs(i - n) for n in c_positions)

        return arr

s = 'loveleetcode'
c = 'e'   
print(Solution().shortestToChar(s,c))
# [3,2,1,0,1,0,0,1,2,2,1,0]