class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-indexed positions
            elif current_sum < target:
                left += 1  # Move the left pointer to the right to increase the sum
            else:
                right -= 1  # Move the right pointer to the left to decrease the sum
        
        return []  # Return empty if no solution is found (though the problem guarantees one solution)
