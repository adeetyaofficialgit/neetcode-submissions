class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for i in range(0, len(nums)):
            isExistCompIndex =  hashMap.get(target-nums[i])
            if(isExistCompIndex != None):
                if(isExistCompIndex < i):
                    return [isExistCompIndex, i]
                else:
                    return [i, isExistCompIndex]
            else:
                hashMap[nums[i]] = i
