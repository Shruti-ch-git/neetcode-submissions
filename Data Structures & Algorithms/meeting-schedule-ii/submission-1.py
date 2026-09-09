class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda interval: interval.start)
        minHeap = []
        rooms = 0
        
        for interval in intervals:

            while minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, interval.end)
            rooms = max(rooms, len(minHeap))
        return rooms




        

        