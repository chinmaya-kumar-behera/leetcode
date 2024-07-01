class Solution(object):
    def compressedString(self, word):
        comp = []
        count = 1
        newCh = word[0]
        for ch in word[1:]:
            if ch == newCh and count < 9:
                count += 1
            else:
                comp.append(str(count))
                comp.append(newCh)
                newCh = ch
                count  = 1
        comp.append(str(count))
        comp.append(newCh)
        return "".join(comp)
        