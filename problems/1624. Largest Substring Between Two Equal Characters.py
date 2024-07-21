class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        m = {}
        maxDis = -1

        for i,ch in enumerate(s):
            if ch in m:
                distance = i - m[ch] - 1
                if distance > maxDis:
                    maxDis = distance
            else:
                m[ch] = i

        return maxDis




sol = Solution()
print(sol.maxLengthBetweenEqualCharacters("abca"))  # Output: 2 (characters 'a' at indices 0 and 3)
print(sol.maxLengthBetweenEqualCharacters("cbzxy"))  # Output: -1 (no repeating characters)
print(sol.maxLengthBetweenEqualCharacters("cabbac"))