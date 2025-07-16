class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstrow="qwertyuiop"
        secondrow="asdfghjkl"
        thirdrow="zxcvbnm"
        ans=[]
        for word in words:
            if all(char.lower() in firstrow for char in word) or all(char.lower() in secondrow for char in word) or all(char.lower() in thirdrow for char in word):
                ans.append(word)
            else:
                continue
        return ans

        