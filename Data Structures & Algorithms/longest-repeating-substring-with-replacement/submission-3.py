class Solution:

    def getMaxFrequency(self, d):
        return max(d.values(), default=0)


    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freqMap = {}
        maxLength = 0

        for right in range(0, len(s)):
            freqMap[s[right]] = freqMap.get(s[right], 0) +1

            while(right-left+1 - self.getMaxFrequency(freqMap) > k and left<right):
                freqMap[s[left]] = freqMap.get(s[left], 0) -1
                left+=1

            maxLength = max(maxLength, right-left+1)
        
        return maxLength



            
        