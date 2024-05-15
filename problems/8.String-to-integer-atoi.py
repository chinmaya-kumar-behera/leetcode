class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        s = s.strip()  # Remove leading and trailing whitespace

        if not s:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        result = 0
        for ch in s:
            if not ch.isdigit():
                break
            result = result * 10 + int(ch)

        result *= sign

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result




        return 

obj = Solution()
res = obj.myAtoi("4193 with words")

print(res)