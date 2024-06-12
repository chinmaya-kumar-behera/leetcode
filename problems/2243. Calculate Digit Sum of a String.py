class Solution:
    def digitSum(self, s, k):
       
        while len(s) > k:
            news = ""
            while len(s) > 0:
                stringWord = s[0:k]
                news += str(sum(map(int,list(stringWord))))
                s = s[k:]
            s = news
        return news

print(Solution().digitSum('11111222223',3))

