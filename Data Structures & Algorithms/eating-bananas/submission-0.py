import math

class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        
        def canFinish(k):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / k)
            return total_hours <= h
        
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid  # Try a smaller k
            else:
                left = mid + 1  # Increase k
        
        return left  # The smallest k that allows Koko to finish within h hours
