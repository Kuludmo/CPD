class Solution:
    def sortSentence(self, s: str) -> str: 
         def isnumber(word):
            number=''
            for i in word:
                 if i.isdigit():
                    number += i
            return number
         array=s.split()
         array=sorted(array, key=isnumber)
         ans=[]
         for i in array:
            x=i[:-1]
            ans.append(x)
         result=' '.join(ans)
         return result