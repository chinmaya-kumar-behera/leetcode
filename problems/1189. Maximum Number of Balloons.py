class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # m = {}

        # for ch in text:
        #     if ch in "balloon":
        #         if ch in m:
        #             m[ch] += 1
        #         else:
        #             m[ch] = 1
        
        # return min(m.get('b',0),m.get('a',0),m.get('l',0)//2,m.get('o',0)//2,m.get('n',0))
            
        b = text.count("b")
        a = text.count("a")
        l = text.count("l")
        o = text.count("o")
        n = text.count("n")

        return min(b, a, l // 2, o // 2, n)
        