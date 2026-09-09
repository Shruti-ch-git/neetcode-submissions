from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i in range(len(lists)):
            node=lists[i]
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
        dummy=ListNode(0)
        tail=dummy
        while minHeap:
            value, position , nodex= heapq.heappop(minHeap)
            tail.next=nodex
            tail=tail.next
            if nodex.next:
                heapq.heappush(minHeap, (nodex.next.val, position, nodex.next))
        return dummy.next


            
        

