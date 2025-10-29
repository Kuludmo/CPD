class Solution(object):
    def mergeAlternately(self, word1, word2):
        merge=[]
        min_word=min(len(word1), len(word2))
        for i in range(min_word):
            merge.append(word1[i])
            merge.append(word2[i])
        merge.append(word1[min_word:])
        merge.append(word2[min_word:])
        return ''.join(merge)
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        