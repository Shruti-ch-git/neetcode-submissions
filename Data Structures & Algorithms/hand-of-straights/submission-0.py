class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize !=0 :
            return False
        h={}
        for i in hand:
            h[i]= h.get(i,0)+1
        minh=list(h.keys())
        heapq.heapify(minh)
        while minh:
            first=minh[0]
            for i in range(first, first+groupSize):
                if i not in h:
                    return False
                h[i]-=1
                if h[i]==0:
                    heapq.heappop(minh)
        return True
                    
                        
                    
                
                
                
        
        
        

        