class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
       import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letter=list(string.ascii_lowercase)
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
              "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
              "..-","...-",".--","-..-","-.--","--.."]
        eng_alphabets={}
        for i in range(len(letter)):
            eng_alphabets[letter[i]]=morse_code[i]
        map=[]
        for i in words:
            w=""
            for j in i:
                w+=eng_alphabets[j]
            map.append(w)
            lyu=set()
            for i in map:
                lyu.add(i)
        return len(lyu)