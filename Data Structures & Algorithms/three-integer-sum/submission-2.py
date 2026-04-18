class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort the array first
        triplets = set()  # To store unique triplets as sets (tuples)

        for i in range(len(nums) - 2):
            # Skip duplicates for the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            target = -nums[i]  # We want nums[left] + nums[right] == -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    triplets.add((nums[i], nums[left], nums[right]))  # Add the triplet to the set
                    left += 1  # Move left pointer to the right
                    right -= 1  # Move right pointer to the left
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1  # We need a larger sum, so move left pointer right
                else:
                    right -= 1  # We need a smaller sum, so move right pointer left

        # Convert the set of triplets to a list and return
        return [list(triplet) for triplet in triplets]
