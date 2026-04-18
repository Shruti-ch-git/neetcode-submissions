class Solution:
    def findMin(self, nums: List[int]) -> int:
        x, y = 0, len(nums) - 1

        while x < y:
            m = (x + y) // 2

            if nums[m] > nums[y]:
                x = m + 1
            else:
                y = m

        return nums[x]