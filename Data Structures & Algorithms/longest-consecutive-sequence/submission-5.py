from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        fMap = Counter(nums)

        starters = []

        biggestCount=0

        for n in fMap.keys():
            if(fMap.get(n-1,0) == 0 and fMap.get(n+1, 0)>=0):
                starters.append(n)
        
        for s in starters:
            count=0
            k=s
            while (fMap.get(k, 0) > 0):
                count+=1
                k+=1
            biggestCount = max(biggestCount, count)
        
        return biggestCount

