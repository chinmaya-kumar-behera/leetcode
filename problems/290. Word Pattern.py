class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        r = {}

        for ch,word in zip(pattern,s.split()):
            if ch in d:
                if d[ch] != word:
                    return False
            else:
                if word in r:
                    return False
                else:
                    d[ch] = word
                    r[word] = ch

        return True

print(Solution().wordPattern("abba","dog cat cat dog"))
print(Solution().wordPattern("abba","dog dog dog dog"))
print(Solution().wordPattern("abba","dog cat cat dog"))
print(Solution().wordPattern("abc","dog cat dog"))