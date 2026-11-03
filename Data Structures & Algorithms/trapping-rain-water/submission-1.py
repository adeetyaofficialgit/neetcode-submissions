class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax = [-1]*len(height)
        rightMax = [-1]*len(height)

        for left in range(0, len(height)):
            if(left == 0):
                leftMax[0] = height[left]
                continue
            leftMax[left] = max(leftMax[left-1], height[left-1])

        #print(leftMax)

        for right in range(len(height)-1, -1, -1):
            if(right == len(height)-1):
                rightMax[-1] = height[right]
                continue
            rightMax[right] = max(rightMax[right+1], height[right+1])

        #print(rightMax)

        waterCollected = 0

        for i in range(0, len(height)):
            waterAtI = min(leftMax[i], rightMax[i]) - height[i]

            if(waterAtI < 0):
                continue

            waterCollected+=waterAtI 

        return waterCollected