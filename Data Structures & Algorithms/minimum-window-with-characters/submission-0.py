from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortestSubstring=None

        freqMapT = Counter(t)
        need = len(freqMapT)

        print("Need", need, freqMapT)

        left = 0
        freqMapS = {}
        have = 0
        for right in range(0, len(s)):
            freqMapS[s[right]] = freqMapS.get(s[right], 0) +1

            if(freqMapS.get(s[right], 0) == freqMapT.get(s[right], 0)):
                have+=1
            
            while(have == need and left <= right):
                currentSubstring = s[left:right+1]

                if shortestSubstring is None or len(currentSubstring) < len(shortestSubstring):
                    shortestSubstring = currentSubstring
                else:
                    shortestSubstring=min(shortestSubstring, currentSubstring, key=len)
                freqMapS[s[left]] = freqMapS.get(s[left], 0) -1
                if(freqMapS.get(s[left],0) < freqMapT.get(s[left], 0)):
                    have-=1
                left+=1
                
        return "" if shortestSubstring is None else shortestSubstring    
        



        