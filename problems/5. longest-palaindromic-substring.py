from typing import *
class Solution:
    def longestPalindrome(self, s: str) -> str:
    	
    	maxWord = ""

    	for i in range(len(s)):
    		for j in range(i+1, len(s)+1):
    			sus = s[i:j]
    			if sus == sus[::-1] and len(maxWord) < len(sus):
    				maxWord = sus
    	return maxWord

	


s = "PAHNAPLSIIGYIR	"
obj = Solution()

result = obj.longestPalindrome(s)

print(result)


	