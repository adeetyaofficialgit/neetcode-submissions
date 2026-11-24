class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s+=str(len(i))+"%"+i
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        decoded = []
        print(s)
        i=0
        numS = ""
        word = ""
        while (i<len(s)):
            if(s[i] == "%"):
                i+=1
                for j in range(0, int(numS)):
                    word+=s[i]
                    i+=1
                decoded.append(word)
                word=""
                numS=""
            else:
                numS+=s[i]
                i+=1
                
            
        return decoded
