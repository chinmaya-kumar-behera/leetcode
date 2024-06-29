class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def removeString(s):
            strArr = []

            for ch in s:
                if ch == "#":
                    if strArr:
                        strArr.pop()
                else:
                    strArr.append(ch)
            return "".join(strArr)
        
        return removeString(s) == removeString(t)




print(Solution().backspaceCompare("y#fo##f","y#f#o##f"))