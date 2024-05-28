class Solution:
    def reverseStr(self, s,k):
        news = ""

        for i in range(0,len(s),k):
            news += s[i:i+k][::-1]

        return news 


print(Solution().reverseStr('abcdefg',2))
        