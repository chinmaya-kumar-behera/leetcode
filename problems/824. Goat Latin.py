class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        news = ""
        for ind in range(len(words)):
            word = words[ind]
            if word[0] in 'aeiouAEIOU':
                news += word+'ma'+('a'*(ind+1))+" "
            else:
                news += word[1:]+word[0]+'ma'+('a'*(ind+1))+" "
        return news[:-1]
    
