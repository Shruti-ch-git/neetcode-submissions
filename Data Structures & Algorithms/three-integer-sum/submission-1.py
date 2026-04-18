class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort the array first
        result = []

        for i in range(len(nums) - 1):
            # Skip duplicates for the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            target = -nums[i]  # We need nums[left] + nums[right] == target

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move left pointer and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move right pointer and skip duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1  # We need a larger sum, so move left pointer right
                else:
                    right -= 1  # We need a smaller sum, so move right pointer left

        return result
