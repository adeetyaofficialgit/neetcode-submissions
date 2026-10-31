class Solution:

    

    def hasDuplicate(self, nums: List[int]) -> bool:

        hashMap = {}

        for i in range(0,len(nums)):
            freq = hashMap.get(nums[i], 0)
            if( freq == 1):
                return True
            else:
                hashMap[nums[i]] = freq+1
        
        return False