from collections import Counter
class Solution:

    def isEqual(self, s1, s2):
        return Counter(s1) == Counter(s2)

    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqMap = {}

        left=0
        #maintain fix window of size s1
        for right in range(len(s1)-1, len(s2)):
            if(self.isEqual(s1, s2[left:right+1])):
                return True
            left+=1
        
        return False
