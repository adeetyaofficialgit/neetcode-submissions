from collections import Counter
class Solution:

    def isEqual(self, s1, s2):
        return Counter(s1) == Counter(s2)

    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqMap = {}

        freqMapsS1 = Counter(s1)
        freqMapsS2 = {}

        left=0
        #maintain fix window of size s1
        for right in range(len(s1)-1, len(s2)):

            if(freqMapsS2 == {}):
                freqMapsS2 = Counter(s2[left: right])
            freqMapsS2[s2[right]] = freqMapsS2.get(s2[right],0)+1

            if(freqMapsS1 == freqMapsS2):
                return True
            freqMapsS2[s2[left]] = freqMapsS2.get(s2[left],0)-1
            left+=1
        
        return False
