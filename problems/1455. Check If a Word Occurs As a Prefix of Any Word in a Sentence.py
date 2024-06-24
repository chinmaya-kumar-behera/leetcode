class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):

        splits = sentence.split()
        for ind in range(len(splits)):
            if searchWord == splits[ind][:len(searchWord)]:
                return ind+1
        return -1         

print(Solution().isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))
        