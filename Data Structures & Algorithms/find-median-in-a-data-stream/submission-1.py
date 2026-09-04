import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap containing the smaller half.
        # Python uses a min-heap, so store negative values.
        self.small = []

        # Min-heap containing the larger half.
        self.large = []

    def addNum(self, num: int) -> None:
        # Decide which half receives num
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        # Rebalance if small has two extra elements
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # Rebalance if large has two extra elements
        elif len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        if len(self.large) > len(self.small):
            return float(self.large[0])

        return (-self.small[0] + self.large[0]) / 2.0