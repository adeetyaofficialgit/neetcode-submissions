from collections import defaultdict, Counter

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        output= []
        freqM = defaultdict(int)

        maxFreq = 0

        for i in nums:
            freqM[i] +=1
            maxFreq = max(maxFreq, freqM[i])

        #print(freqM)

        bucketArray = [[] for _ in range(0, maxFreq+1)]

        #print(bucketArray)

        for key in freqM.keys():
            bucketArray[freqM[key]].append(key)
        
        #print(bucketArray)

        for i in range(len(bucketArray)-1, -1, -1):

            if(k==0):
                return output
            elif(bucketArray[i] == []):
                continue
            else:
                for j in bucketArray[i]:
                    k-=1
                    output.append(j)
                    if(k==0):
                        return output
        
        #print(output)
        return output
        