class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Save curMax before updating it
            temp = curMax

            curMax = max(
                num,                  # Start a new subarray
                num * temp,    # Extend previous maximum
                num * curMin          # Negative × negative
            )

            curMin = min(
                num,
                num * temp,
                num * curMin
            )

            result = max(result, curMax)

        return result