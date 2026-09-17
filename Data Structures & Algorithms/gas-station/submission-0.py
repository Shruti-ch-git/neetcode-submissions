class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            remaining = gas[i] - cost[i]

            total += remaining
            tank += remaining

            # Cannot reach station i + 1 from the current start
            if tank < 0:
                start = i + 1
                tank = 0

        # Overall gas must be enough for the overall cost
        return start if total >= 0 else -1