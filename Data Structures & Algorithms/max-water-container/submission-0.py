class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a=0
        b=len(heights)-1
        max_area=0
        while a<b:
            area=(b-a)*min(heights[a],heights[b])
            max_area=max(area,max_area)
            if heights[a]<heights[b]:
                a+=1
            else:
                b-=1
        return max_area
