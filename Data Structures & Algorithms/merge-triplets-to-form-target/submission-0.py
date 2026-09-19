import heapq
from typing import List

class Solution:
    def mergeTriplets(
        self,
        triplets: List[List[int]],
        target: List[int]
    ) -> bool:

        # Only these triplets can safely be used
        valid = []
        for triplet in triplets:
            if (
                triplet[0] <= target[0]
                and triplet[1] <= target[1]
                and triplet[2] <= target[2]
            ):
                valid.append(triplet)

        if not valid:
            return False

        res = []
        count = 0

        while count < 3:
            maxHeap = []

            for triplet in valid:
                heapq.heappush(maxHeap, -triplet[count])

            res.append(-heapq.heappop(maxHeap))
            count += 1

        return res == target