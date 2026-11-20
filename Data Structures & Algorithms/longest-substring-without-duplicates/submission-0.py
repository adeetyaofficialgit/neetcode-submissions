class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        freqMap = {}
        left=0
        longestSubstringLength=0

        for right in range(0, len(s)):

            freqMap[s[right]] = freqMap.get(s[right],0) +1

            while(freqMap.get(s[right], 0) > 1):
                freqMap[s[left]] = freqMap.get(s[left],0) -1
                left+=1
            
            substringLength = right-left+1 
            longestSubstringLength = max(longestSubstringLength, substringLength)
        
        return longestSubstringLength
