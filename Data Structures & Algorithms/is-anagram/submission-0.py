class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashMap = {}
        if(len(s) != len(t)):
            return False


        for i in range(0, len(s)):
            hashMap[s[i]]= hashMap.get(s[i], 0) + 1
        for j in range(0, len(t)):
            hashMap[t[j]]= hashMap.get(t[j],0) - 1

        for h in hashMap.values():
            if(h > 0):
                return False

        return True