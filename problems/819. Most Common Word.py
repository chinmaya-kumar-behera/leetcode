import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):        
        frequently = ""
        maxCount = 0
        visited = []

        words = re.findall(r'\w+', paragraph.lower())
        
        for word in words:
            if (word not in visited) and word not in banned:
                c = words.count(word)
                if c > maxCount:
                    maxCount = c
                    frequently = word
                    visited.append(word)

        return frequently

        return frequently
        




        

# p = "Bob hit a ball, the hit BALL flew far after it was hit."
p = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
print(Solution().mostCommonWord(p,banned))