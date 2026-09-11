from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            one_step = dp[i - 1] + cost[i - 1]
            two_steps = dp[i - 2] + cost[i - 2]

            dp[i] = min(one_step, two_steps)

        return dp[n]