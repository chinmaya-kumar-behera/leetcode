# from typing import * 
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         strs = sorted(strs,key=len)
#         prefix = strs[0]
        
#         for word in strs[1:]:

#             i = len(prefix)-1

#             for i in range(len(prefix),0,-1):
#                 if word[0] != prefix[0]:
#                     return ""
#                 if word[:i] == prefix[:i]:
#                     prefix = word[:i]
#                     break
        
#         return prefix


from typing import * 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        first=strs[0]
        last=strs[-1]
        prefix = ""

        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                prefix += first[i]
            else:
                break

        return prefix 




obj = Solution()
strs = ["dog","dacecar","dar"]

res = obj.longestCommonPrefix(strs)

print("----------------")
print("output is ",res)