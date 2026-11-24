class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #leftpass
        runningLeftProduct=1
        runningLeftArr = [0 for _ in range(0, len(nums))]
        for i,v in enumerate(nums):
            runningLeftArr[i] = runningLeftProduct
            runningLeftProduct = runningLeftProduct*v
        

         #rightpass
        runningRightProduct=1
        runningRightArr = [0 for _ in range(0, len(nums))]
        for j in range(len(nums)-1, -1, -1):
            v = nums[j]
            runningRightArr[j] = runningRightProduct
            runningRightProduct = runningRightProduct*v
        

        output = [] 
        for n in range(len(nums)):
            output.append(runningLeftArr[n]*runningRightArr[n])
        return output
