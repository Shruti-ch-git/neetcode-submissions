class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        p=0
        while l<r:
            h=min(heights[l],heights[r])
            b= r-l
            p=max(p, h*b)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return p



        