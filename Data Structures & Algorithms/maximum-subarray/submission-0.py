

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        largest = nums[0]

        for r in range(len(nums)):
            # A negative previous sum cannot help the next subarray
            if total < 0:
                total = 0

            total += nums[r]
            largest = max(largest, total)

        return largest