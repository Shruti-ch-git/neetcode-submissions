class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # Initialize the left and right pointers
        
        while l <= r:  # Use l <= r to ensure we check the final index
            m = (l + r) // 2  # Find the midpoint
            
            if nums[m] == target:  # Check if we've found the target
                return m

            if nums[m] <= nums[r]:  # Right half is sorted
                if nums[m] < target <= nums[r]:  # Target is in the sorted right half
                    l = m + 1
                else:  # Target is in the left half
                    r = m - 1
            else:  # Left half is sorted
                if nums[l] <= target < nums[m]:  # Target is in the sorted left half
                    r = m - 1
                else:  # Target is in the right half
                    l = m + 1

        return -1  # Return -1 if the target is not found
