class Solution:
    def isValid(self, s: str) -> bool:
        m = {")":"(","]":"[","}":"{"}
        stack = []

        for ch in s:
            if ch in m.values():
                stack.append(ch)

            elif ch in m:
                if  stack.pop() != m[ch]:
                    return False
        return not stack


obj = Solution()

res = obj.isValid('()(')

print(res)