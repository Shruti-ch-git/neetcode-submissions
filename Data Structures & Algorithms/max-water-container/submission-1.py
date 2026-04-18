class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area with the current left and right bars
            width = right - left
            height = min(heights[left], heights[right])
            current_area = width * height
            
            # Update the maximum area found so far
            max_area = max(max_area, current_area)
            
            # Move the pointer for the shorter bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
