class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # An odd total cannot be divided equally
        if total % 2 != 0:
            return False

        target = total // 2
        possible = {0}

        for num in nums:
            newPossible = set()

            for currentSum in possible:
                newSum = currentSum + num

                if newSum == target:
                    return True

                if newSum < target:
                    newPossible.add(newSum)

            possible.update(newPossible)

        return target in possible