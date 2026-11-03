class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        highestAreaYet = 0

        while(left<right):
            chosenHeight = min(heights[left],heights[right])
            area = (right-left)*chosenHeight
            if(area > highestAreaYet):
                highestAreaYet = area
            
            if(heights[right] == chosenHeight):
                right-=1
            elif(heights[left] == chosenHeight):
                left+=1
                
        return highestAreaYet